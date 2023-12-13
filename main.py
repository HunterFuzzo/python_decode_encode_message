from crc_encode_decode import *
from ascii_encode_decode import *
from binary_encode_decode import *
from manchester_encode_decode import *
from ask_encode_decode import *
import os

class Encoded:
    def __init__(self, message):
        self.message = message
    
    def asciiEncode(self):
        return text_to_ascii(self.message)
    
    def binaryEncode(self):
        return ascii_to_binary(self.asciiEncode())
    
    def crcEncode(self):
        return crc_encode(self.binaryEncode(), data)  # choose divisor
    
    def manchesterEncode(self):
        return crc_to_manchester(self.crcEncode())
    
    def askEncode(self):
        return manchester_to_ask(self.manchesterEncode())

class Decoded:
    def __init__(self, message):
        self.message = message

    def askDecode(self):
        return ask_to_manchester(self.message)

    def manchesterDecode(self):
        return manchester_to_crc(self.askDecode())

    def crcDecode(self):
        return crc_decode(self.manchesterDecode(), data)  # choose divisor

    def binaryDecode(self):
        return binary_to_ascii(self.crcDecode())
    
    def asciiDecode(self):
        return ascii_to_text(self.binaryDecode())

def main():
    messageToEncode = input("Enter a message: ")
    originalMessage = Encoded(message=messageToEncode)
    messageToDecode = originalMessage.manchesterEncode()
    encodedMessage = Decoded(message=messageToDecode)

    print(f"\nMessage: {messageToEncode}")
    print(f"Message to ASCII: {originalMessage.asciiEncode()}")
    print(f"ASCII to binary: {originalMessage.binaryEncode()}")
    print(f"Binary to CRC: {originalMessage.crcEncode()}")
    print(f"CRC to Manchester: {originalMessage.manchesterEncode()}")

    print("\n==================================================================\n")

    print("Signal sent, here's the reception logs: There's no problem during ASK")

    print("\n==================================================================\n")

    print(f"Manchester to CRC: {encodedMessage.manchesterDecode()}")
    print(f"CRC to binary: {encodedMessage.crcDecode()}")
    print(f"Binary to ASCII: {encodedMessage.binaryDecode()}")
    print(f"ASCII to text: {encodedMessage.asciiDecode()}")

if __name__ == "__main__":
    while True:
        os.system('cls')
        main()
        restart = input("\nPress Enter to restart or type 'exit' to quit: ")
        if restart.lower() == "exit":
            break