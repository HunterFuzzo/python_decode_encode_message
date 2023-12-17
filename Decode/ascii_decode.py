def ascii_to_text(encoded_text):
    """
    Convertit une liste d'entiers ASCII en une chaîne de texte.

    Paramètres:
        encoded_text (list): Liste d'entiers représentant les caractères ASCII.

    Renvoie:
        str: Chaîne de texte résultante de la conversion des entiers ASCII.

    Remarque:
        Cette fonction suppose que la liste d'entiers représente des caractères ASCII.
    """
    # Utilise la fonction chr() pour convertir chaque entier en caractère ASCII
    text = ''.join([chr(code) for code in encoded_text])

    # Retourne la chaîne de texte résultante
    return text
