import numpy as np
import sounddevice as sd

def ask_to_manchester(modulated_list):
    """
    Démodule un signal modulé en amplitude (ASK) vers le codage Manchester.

    Paramètres:
        modulated_list (list): Liste de valeurs représentant le signal modulé en amplitude.

    Renvoie:
        list: Liste de valeurs binaires représentant le signal démodulé en codage Manchester.

    Remarque:
        Cette fonction suppose que le signal modulé en amplitude est échantillonné à une fréquence
        de Fe (en Hz), avec une fréquence de bauds (baud) spécifiée. Le codage Manchester est utilisé
        pour la démodulation.
    """
    # Paramètres du signal
    Fe = 44100
    baud = 300
    Ns = int(Fe / baud)

    # Conversion de la liste modulée en un tableau numpy
    modulated_list = np.array(modulated_list)

    # Initialisation de la variable S avec la liste modulée
    S = modulated_list

    # Création du produit modulé
    Produit = modulated_list * S

    # Initialisation de la liste résultante
    Res = []

    # Calcul de l'intégrale (trapèze) sur des segments de Ns échantillons
    for i in range(0, len(modulated_list), Ns):
        Res.append(np.trapz(Produit[i:i+Ns]))

    # Initialisation de la liste de message démodulé en ASK
    message_demodule_ASK = []

    # Conversion des résultats de l'intégrale en valeurs binaires
    for ii in range(0, len(Res)):
        if Res[ii] > 0:
            message_demodule_ASK.extend([int(1)])
        elif Res[ii] <= 0:
            message_demodule_ASK.extend([int(0)])

    # Retourne la liste du message démodulé en ASK
    return message_demodule_ASK