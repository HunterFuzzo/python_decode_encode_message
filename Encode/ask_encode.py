import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

def manchester_to_ask(binaryMessage):
    """
    Convertit une séquence binaire en modulation d'amplitude à décalage de phase (ASK).

    Paramètres:
        binaryMessage (list): Liste de valeurs binaires représentant la séquence binaire.

    Renvoie:
        list: Liste des échantillons de l'ASK résultant de la modulation.
    """
    # Paramètres du signal
    Fe = 44100
    baud = 300
    Nbits = len(binaryMessage)
    Ns = int(Fe / baud)
    N = int(Nbits * Ns)

    # Duplique la séquence binaire pour correspondre à la fréquence d'échantillonnage
    M_duplique = np.repeat(binaryMessage, Ns)

    # Crée le vecteur de temps
    t = np.linspace(0, N / Fe, N)

    # Paramètres de l'onde porteuse
    Ap = 1
    Fp = 19000
    Porteuse = Ap * np.sin(2 * np.pi * Fp * t)

    # Modulation ASK
    ASK = M_duplique * Porteuse

    sd.play(ASK, Fe)
    sd.wait()
    # Affichage des signaux
    plt.figure(figsize=(10, 8))

    plt.subplot(4, 1, 1)
    plt.plot(t, M_duplique, 'red')
    plt.title('Message binaire')
    plt.xlabel('Temps (s)')
    plt.ylabel('Amplitude')
    plt.grid()

    # Subplot 2: Onde Porteuse
    plt.subplot(4, 1, 2)
    plt.plot(t, Porteuse, 'green')
    plt.title('Onde Porteuse')
    plt.xlabel('Temps (s)')
    plt.ylabel('Amplitude')
    plt.grid()

    # Subplot 3: Résultat ASK
    plt.subplot(4, 1, 3)
    plt.plot(t, ASK, 'b')
    plt.title('Résultat ASK')
    plt.xlabel('Temps (s)')
    plt.ylabel('Amplitude')
    plt.grid()

    # Subplot 4: Frequency Spectrum of Carrier Signal
    plt.subplot(4, 1, 4)
    frequencies, spectrum = plt.psd(Porteuse, NFFT=4096, Fs=Fe)
    plt.plot(frequencies, 10 * np.log10(spectrum))  # Convert power to dB
    plt.title('Frequency Spectrum of Carrier Signal')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power/Frequency (dB/Hz)')


    # Affiche les graphiques
    plt.tight_layout()
    plt.show()


    # Retourne la liste des échantillons de l'ASK résultant de la modulation
    return list(ASK)