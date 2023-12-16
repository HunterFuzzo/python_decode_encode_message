"""
    Cette fonction réalise une opération XOR entre deux valeurs binaires.

    @param a: Première valeur binaire
    @param b: Deuxième valeur binaire
    @return Résultat de l'opération XOR entre a et b

    Exemple d'utilisation :
    @code
        xor(1, 0)
    @endcode
"""
def xor(a, b): 
    return a ^ b

data = [1, 0, 1, 1]

"""
    Cette fonction encode une séquence de données avec une division de CRC.

    @param data: Séquence de données à encoder
    @param divisor: Diviseur utilisé dans l'opération de CRC
    @return Séquence de données encodée avec le code CRC

    Exemple d'utilisation :
    @code
        crc_encode([1, 0, 1, 1], [1, 0, 1])
    @endcode
"""
def crc_encode(data, divisor):
    data_extended = data + [0] * (len(divisor) - 1)
    for i in range(len(data)):
    
        if data_extended[i] == 1:
            for j in range(len(divisor)):
                data_extended[i + j] = xor(data_extended[i + j], divisor[j])
    return data + data_extended[-(len(divisor)-1):]

"""
    Cette fonction décode une séquence de données encodée avec le code CRC.

    @param data: Séquence de données à décoder
    @param divisor: Diviseur utilisé dans l'opération de CRC
    @return Séquence de données décodée avec le code CRC, ou affiche une erreur si la détection échoue

    Exemple d'utilisation :
    @code
        crc_decode([1, 0, 1, 1], [1, 0, 1])
    @endcode
"""
def crc_decode(data, divisor):
    data_extended = crc_encode(data, divisor)
    data_extended = data_extended[:-(len(divisor)-1)]

    for i in range(len(data)):
    
        if data_extended[i] == 1:
            for j in range(len(divisor)):
                data_extended[i + j] = xor(data_extended[i + j], divisor[j])
    print(data_extended)

    if data_extended[-(len(divisor)-1):] == [0] * (len(divisor) - 1):
        return data[:-(len(divisor)-1)]
    else:
        print("error during decoding...")
