class TransmissionSequence:
    def __init__(self, message):
        self.message = message
    
    def getMessage(self):
        return f"Voici le message : {self.message}"

enteredMessage = input(str("Entrez un message a décodé : "))

messageCode = TransmissionSequence(message = enteredMessage)

print(messageCode.getMessage())


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