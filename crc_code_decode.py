def xor(a, b):
    # Fonction XOR pour effectuer l'opération bit à bit
    return a ^ b

def crc_encode(data, divisor):
    # Ajout de bits de redondance à la fin des données
    data_extended = data + [0] * (len(data) - 1)
    print("Données originales avec bits de redondance ajoutés:", data_extended)
    
    # Division des données étendues par le diviseur
    for i in range(len(data)):
    
        if data_extended[i] == 1:
            print(f"Iteration {i + 1}:")
            print("  Avant XOR :", data_extended)
            
            # XOR des données étendues avec le diviseur
            for j in range(len(divisor)):
                data_extended[i + j] = xor(data_extended[i + j], divisor[j])
                
            print("  Après XOR :", data_extended)

    # Renvoie les données étendues (bits de redondance ajoutés)
    return data_extended

# Exemple d'utilisation
data = [1, 1, 0, 1, 1]  # Séquence de données
divisor = [1, 0, 1, 1]  # Polynôme générateur (diviseur)

encoded_data = crc_encode(data, divisor)

final_data = data + encoded_data[-(len(data)-1):] # data + CRC

print("Bits de redondance ajoutés (données étendues):", encoded_data)
print(f"Voici le code encodé: {final_data}")
print("\n")

print("""##########################################################################################
##########################################################################################
##########################################################################################\n""")

def crc_decode(received_data, divisor):
        # Ajout de bits de redondance à la fin des données
    data_extended = final_data
    print("Données originales avec bits de redondance ajoutés:", data_extended)
    
    # Division des données étendues par le diviseur
    for i in range(len(data)):
    
        if data_extended[i] == 1:
            print(f"Iteration {i + 1}:")
            print(f"Avant XOR : {data_extended}" )
            
            # XOR des données étendues avec le diviseur
            for j in range(len(divisor)):
                data_extended[i + j] = xor(data_extended[i + j], divisor[j])
                
            print("  Après XOR :", data_extended)

    # Renvoie les données étendues (bits de redondance ajoutés)
    return data_extended

decoded_code = crc_decode(final_data, divisor)

final_code = data + decoded_code[-(len(data)-1):]

print(f"\nVoici le code décodé sans data {decoded_code}")

print(f"Voici le code décodé avec data {final_code}\n")

if decoded_code[-(len(data)-1):] == [0] * (len(data) - 1):
    print("Le code CRC est le même")
else:
    print("Le code CRC n'est pas le même")

print("zebi")