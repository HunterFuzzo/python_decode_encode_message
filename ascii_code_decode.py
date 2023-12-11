"""
    Cette fonction permet de convertir un texte en ASCII

    @param text: texte à encoder en ASCII
    @return texte encodé en ASCII

    Exemple d'utilisation :
    @code
        ascii_encode("hello world!")
    @endcode

"""

def text_to_ascii(text):
    return [ord(char) for char in text]

"""
    Cette fonction permet de convertir de l'ASCII en texte

    @param encoded_text: ASCII à décoder
    @return Un message

    Exemple d'utilisation :
    @code
        ascii_decode([72, 101, 108, 108])
    @endcode

"""

def ascii_to_text(encoded_text):
    return ''.join([chr(code) for code in encoded_text])