def manchester_to_crc(encoded_list):
    """
    Convertit une séquence encodée en codage Manchester en une liste décodée.

    Paramètres:
        encoded_list (list): Liste de valeurs binaires représentant la séquence encodée en Manchester.

    Renvoie:
        list: Liste décodée résultante de la conversion de la séquence Manchester.

    Remarque:
        Cette fonction suppose que la séquence Manchester est encodée avec une alternance de 0 et 1.
        Les séquences invalides sont simplement ignorées.
    """
    # Initialisation de la liste décodée
    decoded_list = []

    # Initialisation de l'index pour parcourir la séquence encodée
    i = 0

    # Parcours de la séquence encodée
    while i < len(encoded_list):
        # Vérification des conditions Manchester (0 suivi de 1 ou 1 suivi de 0)
        if encoded_list[i] == 0 and encoded_list[i + 1] == 1:
            decoded_list.append(0)
        elif encoded_list[i] == 1 and encoded_list[i + 1] == 0:
            decoded_list.append(1)
        
        # Passage au prochain couple d'échantillons
        i += 2

    # Retourne la liste décodée
    return decoded_list
