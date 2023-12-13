"""
    Cette fonction permet de convertir une liste de bits en code de manchester

    @param binary_list: Liste de bits à encoder avec le code de manchester
    @return Un message

    Exemple d'utilisation :
    @code
        crc_to_manchester([0, 1, 0, 1, 1])
    @endcode

"""
def crc_to_manchester(binary_list):
    encoded_list = []
    for bit in binary_list:
        if bit == 0:
            encoded_list.extend([0, 1])  # '01'
        else:
            encoded_list.extend([1, 0])  # '10'
    return encoded_list

"""
    Cette fonction permet de convertir une liste de nombre ascii en bits

    @param encoded_list: Liste de bits à encoder avec le code de manchester
    @return Un message

    Exemple d'utilisation :
    @code
        manchester_to_crc([0, 1, 0, 1, 1])
    @endcode

"""

def manchester_to_crc(encoded_list):
    decoded_list = []
    i = 0
    while i < len(encoded_list):
        if encoded_list[i] == 0 and encoded_list[i + 1] == 1:
            decoded_list.append(0)
        elif encoded_list[i] == 1 and encoded_list[i + 1] == 0:
            decoded_list.append(1)
        else:
            raise ValueError("Invalid Manchester encoding sequence")
        i += 2
    return decoded_list