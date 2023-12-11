from crc_code_decode import *
from ascii_code_decode import *
from binary_code_decode import *

class Encode:
    def __init__(self, message):
        self.message = message
    
    def asciiEncode(self):
        return text_to_ascii(self.message)
    
    def binaryEncode(self):
        return ascii_to_binary(self.asciiEncode())
    
    def crcEncode(self):
        return crc_encode(self.binaryEncode(), [1, 0, 1, 1]) # choose divisor
 

class Decode:
    def __init__(self, message):
        self.message = message

    def asciiDecode(self):
        return ascii_to_text(self.binaryDecode())
    
    def binaryDecode(self):
        return binary_to_ascii(self.crcEncode())
    
    def crcEncode(self):
        return crc_encode([0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1]) # choose divisor


messageToEncode = "Bonjour"
originalMessage = Encode(message = messageToEncode)
#encodedMessage = Decode(message = [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

print(f"Message : {messageToEncode}")
print(f"Message to Ascii : {originalMessage.asciiEncode()}")
print(f"Ascii to binary : {originalMessage.binaryEncode()}")
print(f"Binary to crc : {originalMessage.crcEncode()}")

#print(f"Message decoded in asii to text : {encodedMessage.crcDecode()}")

# etc ...

# can't do  decode now cuz it's the opposite and we need to finish the whole shit