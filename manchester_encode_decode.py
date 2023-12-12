"""
    Cette fonction permet de convertir une liste de bits en code de manchester

    @param binary_list: Liste de bits à encoder avec le code de manchester
    @return Un message

    Exemple d'utilisation :
    @code
        crc_to_manchester([0, 1, 0, 1, 1])
    @endcode

"""

def convertManchester(binary_list):
    return [1 if bit == 0 else 0 for bit in binary_list]