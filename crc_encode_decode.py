def xor(a, b): 
    return a ^ b

data = [1, 0, 1, 1]

def crc_encode(data, divisor):
    data_extended = data + [0] * (len(divisor) - 1)
    for i in range(len(data)):
    
        if data_extended[i] == 1:
            for j in range(len(divisor)):
                data_extended[i + j] = xor(data_extended[i + j], divisor[j])
    return data + data_extended[-(len(divisor)-1):]

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
