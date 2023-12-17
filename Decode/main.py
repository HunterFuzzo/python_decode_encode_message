from crc_decode import *
from ascii_decode import *
from binary_decode import *
from manchester_decode import *
from ask_decode import *

import ast
import tkinter as tk
from tkinter import ttk

import requests
import base64

class Decoded:
    def __init__(self, message):
        """
        Classe pour décodage successif d'un message binaire.

        Paramètres:
            message (list): Message binaire à décoder.
        """
        self.message = message

    def askDecode(self):
        """
        Décodage ASK (Amplitude Shift Keying).

        Renvoie:
            list: Message décodé en ASK.
        """
        return ask_to_manchester(self.message)

    def manchesterDecode(self):
        """
        Décodage Manchester.

        Renvoie:
            list: Message décodé en Manchester.
        """
        return manchester_to_crc(self.askDecode())

    def crcDecode(self):
        """
        Décodage CRC (Cyclic Redundancy Check).

        Renvoie:
            list: Message décodé après vérification CRC.
        """
        return crc_decode(self.manchesterDecode(), [1, 0, 1, 1])

    def binaryDecode(self):
        """
        Décodage binaire vers ASCII.

        Renvoie:
            list: Message décodé en ASCII.
        """
        return binary_to_ascii(self.crcDecode())
    
    def asciiDecode(self):
        """
        Décodage ASCII vers texte.

        Renvoie:
            str: Message décodé en texte.
        """
        return ascii_to_text(self.binaryDecode())

def get_file_content():
    """
    Récupère le contenu d'un fichier depuis une URL GitHub.

    Renvoie:
        str: Contenu du fichier.
    """
    api_url = "https://api.github.com/repos/hunterfuzzo/getnode/contents/main"

    headers = {
        "Authorization": "Bearer token",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        file_content = base64.b64decode(response_data["content"]).decode("utf-8")
        return file_content
    else:
        return "Problème de liaison au canal de transmission, veuillez réessayer plus tard."

def refresh_logs():
    """
    Actualise les logs avec les étapes de décodage successives.
    """
    messageToDecode = ast.literal_eval(get_file_content())
    encodedMessage = Decoded(message=messageToDecode)

    logs = (
        f"Manchester to CRC: {encodedMessage.manchesterDecode()}\n"
        f"CRC to binary: {encodedMessage.crcDecode()}\n"
        f"Binary to ASCII: {encodedMessage.binaryDecode()}\n"
        f"ASCII to text: {encodedMessage.asciiDecode()}"
    )

    logs_text.delete(1.0, tk.END)
    logs_text.insert(tk.END, logs)

# Crée la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Escape No Game - Decoder")
fenetre.minsize(300, 400)

# Crée les onglets
notebook = ttk.Notebook(fenetre)
notebook.pack(expand=True, fill="both")

# Deuxième onglet - Logs
logs_tab = ttk.Frame(notebook)
notebook.add(logs_tab, text="Logs")

logs_text = tk.Text(logs_tab, wrap="word", height=20, width=40)
logs_text.grid(row=0, column=0, padx=10, pady=10)

# Affichage initial des logs
refresh_logs()

# Bouton de rafraîchissement
refresh_button = tk.Button(logs_tab, text="Rafraichir", command=refresh_logs)
refresh_button.grid(row=1, column=0, pady=5)

# Exécute la boucle principale
fenetre.mainloop()
