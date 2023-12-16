"""
    Cette fonction convertit une liste d'entiers ASCII en une liste de bits.

    @param ascii_list: Liste d'entiers ASCII à convertir
    @return Une liste de bits représentant la séquence binaire correspondante

    Exemple d'utilisation :
    @code
        ascii_to_binary([65, 66, 67])
    @endcode
"""
def ascii_to_binary(ascii_list):
    binary_string = ' '.join(format(code, '08b') for code in ascii_list).replace(" ", "")
    return [int(bit) for bit in binary_string]

"""
    Cette fonction convertit une liste de bits en une liste d'entiers ASCII.

    @param binary_list: Liste de bits à convertir
    @return Une liste d'entiers ASCII décodés

    Exemple d'utilisation :
    @code
        binary_to_ascii([01001000, 01100101, 01101100, 01101100, 01101111])
    @endcode

"""
def binary_to_ascii(binary_list):
    binary_string = ''.join(map(str, binary_list))
    chunks = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    ascii_list = [int(chunk, 2) for chunk in chunks]
    return ascii_list
