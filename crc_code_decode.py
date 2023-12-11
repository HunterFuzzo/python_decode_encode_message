def xor(a, b):
    # Fonction XOR pour effectuer l'opération bit à bit
    return a ^ b

def crc_encode(data, divisor):
    # Ajout de bits de redondance à la fin des données
    data_extended = data + [0] * (len(data) - 1)
    # Division des données étendues par le diviseur
    for i in range(len(data)):
    
        if data_extended[i] == 1:
            # XOR des données étendues avec le diviseur
            for j in range(len(divisor)):
                data_extended[i + j] = xor(data_extended[i + j], divisor[j])
    return data + data_extended[-(len(data)-1):] # data + CRC

# Exemple d'utilisation
# data = [1, 1, 0, 1, 1]  # Séquence de données
# divisor = [1, 0, 1, 1]  # Polynôme générateur (diviseur)

# print(crc_encode(data, divisor))


def crc_decode(data, divisor):
    # Ajout de bits de redondance à la fin des données
    data_extended = crc_encode(data, divisor)
    
    # Division des données étendues par le diviseur
    for i in range(len(data)):
    
        if data_extended[i] == 1:
            
            # XOR des données étendues avec le diviseur
            for j in range(len(divisor)):
                data_extended[i + j] = xor(data_extended[i + j], divisor[j])

    final_data = data + data_extended[-(len(data)-1):]
    if final_data[-(len(data)-1):] == [0] * (len(data) - 1):
        return data
    else:
        print("error during decoding...")

#print(crc_decode(data, divisor))
