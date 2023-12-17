def xor(a, b):
    """
    Effectue l'opération XOR entre deux valeurs binaires.

    Paramètres:
        a (int): Valeur binaire (0 ou 1).
        b (int): Valeur binaire (0 ou 1).

    Renvoie:
        int: Résultat de l'opération XOR entre a et b.
    """
    return a ^ b


def crc_decode(data, divisor):
    """
    Décode les données à l'aide de la vérification de redondance cyclique (CRC).

    Paramètres:
        data (list): Liste de valeurs binaires représentant les données encodées.
        divisor (list): Liste de valeurs binaires représentant le diviseur CRC.

    Renvoie:
        list: Données décodées après la vérification et la correction des erreurs CRC.

    Lève:
        ValueError: Si la longueur du diviseur est inférieure à 2.

    Remarque:
        Cette fonction suppose que les données d'entrée ont été encodées à l'aide de CRC
        et peuvent contenir des erreurs qui doivent être corrigées lors du décodage.
    """
    # Vérifie si la longueur du diviseur est valide
    if len(divisor) < 2:
        raise ValueError("La longueur du diviseur doit être d'au moins 2.")

    # Étend les données avec des zéros pour correspondre à la longueur du diviseur
    data_extended = data + [0] * (len(divisor) - 1)

    # Effectue le décodage CRC
    for i in range(len(data)):
        if data_extended[i] == 1:
            for j in range(len(divisor)):
                if i + j < len(data_extended):
                    data_extended[i + j] = xor(data_extended[i + j], divisor[j])

    # Vérifie la condition de fin du décodage
    if data_extended[-(len(divisor) - 1):] == [0] * (len(divisor) - 1):
        return data[:-(len(divisor) - 1)]  # Retourne les données décodées
    else:
        print("Erreur pendant le décodage...")  # Affiche un message d'erreur
