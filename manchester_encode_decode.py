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
    return [1 if bit == 0 else 0 for bit in binary_list]

"""
    Cette fonction permet de convertir une liste de bits en une autre liste de bits

    @param manchester_list: Liste de bits 
    @return Un message

    Exemple d'utilisation :
    @code
        manchester_to_crc([1, 0, 1, 0, 0])
    @endcode

"""

def manchester_to_crc(manchester_list):
    return [1 if bit == 0 else 0 for bit in manchester_list]