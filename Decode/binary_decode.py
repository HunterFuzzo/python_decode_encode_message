def binary_to_ascii(binary_list):
    """
    Convertit une liste de valeurs binaires en une liste d'entiers ASCII.

    Paramètres:
        binary_list (list): Liste de valeurs binaires représentant les caractères ASCII.

    Renvoie:
        list: Liste d'entiers représentant les caractères ASCII correspondants.

    Remarque:
        Cette fonction suppose que la liste binaire est formatée de manière à représenter
        des caractères ASCII en chunks de 8 bits (1 octet) chacun.
    """
    # Convertit la liste binaire en une chaîne binaire
    binary_string = ''.join(map(str, binary_list))

    # Divise la chaîne binaire en chunks de 8 bits
    chunks = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]

    # Convertit chaque chunk binaire en entier ASCII
    ascii_list = [int(chunk, 2) for chunk in chunks]

    # Retourne la liste d'entiers ASCII
    return ascii_list
