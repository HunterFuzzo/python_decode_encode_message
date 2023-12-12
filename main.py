from crc_encode_decode import *
from ascii_encode_decode import *
from binary_encode_decode import *
from manchester_encode_decode import *
from ask_encode_decode import *

class Encode:
    def __init__(self, message):
        self.message = message
    
    def asciiEncode(self):
        return text_to_ascii(self.message)
    
    def binaryEncode(self):
        return ascii_to_binary(self.asciiEncode())
    
    def crcEncode(self):
        return crc_encode(self.binaryEncode(), [1, 0, 1, 1]) # choose divisor
    
    def manchesterEncode(self):
        return crc_to_manchester(self.crcEncode())
    
    def askEncode(self):
        return manchester_to_ask(self.manchesterEncode())

class Decode:
    def __init__(self, message):
        self.message = message

    def askDecode(self):
        return ask_to_manchester(self.message)

    def manchesterDecode(self):
        return manchester_to_crc(self.askDecode())

    def crcDecode(self):
        return crc_decode(self.manchesterDecode(), [1, 0, 1, 1]) # choose divisor

    def binaryDecode(self):
        return binary_to_ascii(self.crcDecode())
    
    def asciiDecode(self):
        return ascii_to_text(self.binaryDecode())
    
messageToEncode = input(str("Enter a message : "))
originalMessage = Encode(message=messageToEncode)
messageToDecode = originalMessage.manchesterEncode()
encodedMessage = Decode(message=messageToDecode)

print(f"Message : {messageToEncode}")
print(f"Message to ASCII : {originalMessage.asciiEncode()}")
print(f"Message to CRC : {originalMessage.crcEncode()}")

print(f"ASCII to binary : {originalMessage.binaryEncode()}")
print(f"Binary to CRC : {originalMessage.crcEncode()}")
print(f"CRC to Manchester : {originalMessage.manchesterEncode()}")

print("\n==================================================================\n")

print("Signal sent, here's the reception logs : There's no problem during ASK")

print("\n==================================================================\n")

print(f"Manchester to CRC : {encodedMessage.manchesterDecode()}")
print(f"CRC to binary : {encodedMessage.crcDecode()}")
print(f"Binary to ASCII : {encodedMessage.binaryDecode()}")
print(f"ASCII to text : {encodedMessage.asciiDecode()}")