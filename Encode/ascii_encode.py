def text_to_ascii(text):
    """
    Convertit une chaîne de texte en une liste d'entiers ASCII.

    Paramètres:
        text (str): Chaîne de texte à convertir.

    Renvoie:
        list: Liste d'entiers représentant les caractères ASCII de la chaîne de texte.

    Remarque:
        Cette fonction utilise la fonction ord() pour obtenir le code ASCII de chaque caractère.
    """
    # Utilise la fonction ord() pour obtenir le code ASCII de chaque caractère
    ascii_list = [ord(char) for char in text]

    # Retourne la liste d'entiers ASCII
    return ascii_list
