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

    def crcDecode(self):
        return crc_decode(self.message, [1, 0, 1, 1]) # choose divisor

    def binaryDecode(self):
        return binary_to_ascii(self.crcDecode())

    def asciiDecode(self):
        return ascii_to_text(self.binaryDecode())
    
messageToEncode = "Bonjour"
messageToDecode = [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
originalMessage = Encode(message = messageToEncode)
encodedMessage = Decode(message = messageToDecode)

# print(f"Message : {messageToEncode}")
# print(f"Message to Ascii : {originalMessage.asciiEncode()}")
# print(f"Ascii to binary : {originalMessage.binaryEncode()}")
# print(f"Binary to crc : {originalMessage.crcEncode()}")

print(f"Crc to binary : {encodedMessage.crcDecode()}")
print(f"Binary to ascii : {encodedMessage.binaryDecode()}")
print(f"Ascii to text : {encodedMessage.asciiDecode()}")



# etc ...
# can't do  decode now cuz it's the opposite and we need to finish the whole shit