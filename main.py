class TransmissionSequence:
    def __init__(self, message):
        self.message = message
    
    def getMessage(self):
        return f"Voici le message : {self.message}"

enteredMessage = "bonjour coucou"


print(TransmissionSequence(message = enteredMessage).getMessage())



# Chaine de transmission 
# Méthode de conversion ASCII
# CAN/CNA
# CRC : 
# Codage CRC
# Décodage CRC
# Manchester :
# Codage Manchester
# Décodage Manchester
# ASK :
# Modulation ASK
# Démodulation ASK

"""
Vous prendrez un exemple de message simple (un seul caractère ASCII)
pour montrer l'ensemble des transformations nécessaires pour réaliser
son envoi puis sa reconstruction à la réception.
"""