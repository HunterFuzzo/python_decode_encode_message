"""
    Cette fonction permet de convertir un texte en ASCII

    @param text: texte à encoder en ASCII
    @return texte encodé en ASCII

    Exemple d'utilisation :
    @code
        ascii_encode("hello world!")
    @endcode

"""

def ascii_encode(text):
    return [ord(char) for char in text]

encoded_result = ascii_encode("Hello, ASCII!")
print(f"Encoded ASCII: {encoded_result}")

"""
    Cette fonction permet de convertir de l'ASCII en texte

    @param encoded_text: ASCII à décoder
    @return Un message

    Exemple d'utilisation :
    @code
        ascii_decode([72, 101, 108, 108])
    @endcode

"""

def ascii_decode(encoded_text):
    return ''.join([chr(code) for code in encoded_text])

decoded_result = ascii_decode([72, 101, 108, 108, 111, 44, 32, 65, 83, 67, 73, 73, 33])
print(f"Decoded ASCII: {decoded_result}")