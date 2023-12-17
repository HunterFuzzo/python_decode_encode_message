import tkinter as tk
from tkinter import ttk
import requests
import base64

from crc_encode import *
from ascii_encode import *
from binary_encode import *
from manchester_encode import *
from ask_encode import *

class Encoded:
    def __init__(self, message):
        """
        Classe pour l'encodage successif d'un message.

        Paramètres:
            message (str): Message à encoder.
        """
        self.message = message
    
    def asciiEncode(self):
        """
        Encode le message en ASCII.

        Renvoie:
            list: Liste des entiers ASCII résultants de l'encodage.
        """
        return text_to_ascii(self.message)
    
    def binaryEncode(self):
        """
        Encode le message ASCII en binaire.

        Renvoie:
            list: Liste des valeurs binaires résultantes de l'encodage binaire.
        """
        return ascii_to_binary(self.asciiEncode())
    
    def crcEncode(self):
        """
        Encode le message binaire en utilisant la vérification CRC.

        Renvoie:
            list: Liste des valeurs binaires résultantes de l'encodage CRC.
        """
        return crc_encode(self.binaryEncode(), [1, 0, 1, 1])  # Choisissez le diviseur
    
    def manchesterEncode(self):
        """
        Encode le message CRC en utilisant la modulation Manchester.

        Renvoie:
            list: Liste des valeurs binaires résultantes de l'encodage Manchester.
        """
        return crc_to_manchester(self.crcEncode())
    
    def askEncode(self):
        """
        Encode le message Manchester en modulation ASK.

        Renvoie:
            list: Liste des échantillons de l'ASK résultants de l'encodage ASK.
        """
        return manchester_to_ask(self.manchesterEncode())

def update_file_in_repository(repo_owner, repo_name, file_path, new_content, commit_message, access_token):
    """
    Met à jour le contenu d'un fichier dans un dépôt GitHub.

    Paramètres:
        repo_owner (str): Propriétaire du dépôt.
        repo_name (str): Nom du dépôt.
        file_path (str): Chemin du fichier à mettre à jour.
        new_content (str): Nouveau contenu du fichier.
        commit_message (str): Message du commit.
        access_token (str): Jeton d'accès GitHub.
    """
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(api_url, headers=headers)
    response_data = response.json()

    if response.status_code == 200:  # Si la requête a réussi
        sha = response_data["sha"]

        updated_content = base64.b64encode(new_content.encode("utf-8")).decode("utf-8")

        payload = {
            "message": commit_message,
            "content": updated_content,
            "sha": sha
        }

        response = requests.put(api_url, json=payload, headers=headers)
        
        if response.status_code == 200:  # Si la requête a réussi
            result_label.config(text="Status du message : Le message a bien été envoyé.")
        else:   
            result_label.config(text="Status du message : Le message n'a pas pu être envoyé.")
    else:
        return

def encode_and_update_repository():
    """
    Encode le message entré et met à jour le dépôt GitHub avec le résultat.
    """
    message_to_encode = entered_message.get()
    original_message = Encoded(message=message_to_encode)

    logs = (
        f"\nMessage: {message_to_encode}\n"
        f"Message to ASCII: {original_message.asciiEncode()}\n"
        f"ASCII to binary: {original_message.binaryEncode()}\n"
        f"Binary to CRC: {original_message.crcEncode()}\n"
        f"CRC to Manchester: {original_message.manchesterEncode()}\n"
        "Le signal a bien été envoyé au canal de transmission, aucune erreur durant la modulation ASK"
    )

    update_file_in_repository("hunterfuzzo", "getnode", "main", str(original_message.askEncode()), "Update file via API", "token")

    logs_text.delete(1.0, tk.END)
    logs_text.insert(tk.END, logs)

# Crée la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Escape No Game - Encoder")
fenetre.minsize(300, 400)

# Crée les onglets
notebook = ttk.Notebook(fenetre)
notebook.pack(expand=True, fill="both")

# Premier onglet - Input
input_tab = ttk.Frame(notebook)
notebook.add(input_tab, text="Input")

label = tk.Label(input_tab, text="Enter a message to encode:")
label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

entered_message = tk.StringVar()
entry = tk.Entry(input_tab, textvariable=entered_message)
entry.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(input_tab, text="Message status: ")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

encode_button = tk.Button(input_tab, text="Envoyer", command=encode_and_update_repository)
encode_button.grid(row=2, column=0, columnspan=2, pady=10)

# Deuxième onglet - Logs
logs_tab = ttk.Frame(notebook)
notebook.add(logs_tab, text="Logs")

logs_text = tk.Text(logs_tab, wrap="word", height=20, width=40)
logs_text.grid(row=0, column=0, padx=10, pady=10)

# Fonction pour effacer les logs lors du passage à l'onglet "Logs"
def tab_changed(event):
    current_tab = notebook.select()
    if current_tab == logs_tab:
        logs_text.delete(1.0, tk.END)

notebook.bind("<<NotebookTabChanged>>", tab_changed)

# Exécute la boucle principale
fenetre.mainloop()
