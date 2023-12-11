import tkinter as tk

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
    
def startEvent():
    messageToEncode = entry.get()
    originalMessage = Encode(message=messageToEncode)
    messageToDecode = originalMessage.manchesterEncode()
    encodedMessage = Decode(message=messageToDecode)

    label1.config(text=f"Message : {messageToEncode}")
    label2.config(text=f"Message to ASCII : {originalMessage.asciiEncode()}")
    label3.config(text=f"Message to CRC : {originalMessage.crcEncode()}")

    label4.config(text=f"ASCII to binary : {originalMessage.binaryEncode()}")
    label5.config(text=f"Binary to CRC : {originalMessage.crcEncode()}")
    label6.config(text=f"CRC to Manchester : {originalMessage.manchesterEncode()}")

    label7.config(text="Signal sent, here's the reception logs :")
    label8.config(text=f"ASK to Manchester : {encodedMessage.askDecode()}")

    label9.config(text=f"Manchester to CRC : {encodedMessage.manchesterDecode()}")
    label10.config(text=f"CRC to binary : {encodedMessage.crcDecode()}")
    label11.config(text=f"Binary to ASCII : {encodedMessage.binaryDecode()}")
    label12.config(text=f"ASCII to text : {encodedMessage.asciiDecode()}")

root = tk.Tk()
root.title("Encoder - Decoder")

root.minsize(400, 500)

label = tk.Label(root, text="Enter your message :")
label.grid(row=0, column=0, pady=10, columnspan=2)

label1 = tk.Label(root, text="Message : ")
label1.grid(row=2, column=0, pady=10, sticky=tk.W)
label2 = tk.Label(root, text="Message to ASCII : ")
label2.grid(row=3, column=0, pady=10, sticky=tk.W)
label3 = tk.Label(root, text="Message to CRC : ")
label3.grid(row=4, column=0, pady=10, sticky=tk.W)

label4 = tk.Label(root, text="ASCII to binary : ")
label4.grid(row=2, column=1, pady=10, sticky=tk.W)
label5 = tk.Label(root, text="Binary to CRC : ")
label5.grid(row=3, column=1, pady=10, sticky=tk.W)
label6 = tk.Label(root, text="CRC to Manchester : ")
label6.grid(row=4, column=1, pady=10, sticky=tk.W)

label7 = tk.Label(root, text="Signal sent, here's the reception logs :")
label7.grid(row=6, column=0, pady=10, columnspan=2, sticky=tk.W)

label8 = tk.Label(root, text="ASK to Manchester : ")
label8.grid(row=7, column=0, pady=10, columnspan=2, sticky=tk.W)

label9 = tk.Label(root, text="Manchester to CRC : ")
label9.grid(row=8, column=0, pady=10, columnspan=2, sticky=tk.W)
label10 = tk.Label(root, text="CRC to binary : ")
label10.grid(row=9, column=0, pady=10, columnspan=2, sticky=tk.W)
label11 = tk.Label(root, text="Binary to ASCII : ")
label11.grid(row=10, column=0, pady=10, columnspan=2, sticky=tk.W)
label12 = tk.Label(root, text="ASCII to text : ")
label12.grid(row=11, column=0, pady=10, columnspan=2, sticky=tk.W)

entry = tk.Entry(root)
entry.grid(row=1, column=0, pady=10, columnspan=2)

button = tk.Button(root, text="Submit", command=startEvent)
button.grid(row=5, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()