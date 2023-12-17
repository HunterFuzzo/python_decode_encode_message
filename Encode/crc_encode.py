def xor(a, b):
    return a ^ b

def crc_encode(data, divisor):
    data_extended = data + [0] * (len(divisor) - 1)
    for i in range(len(data)):
        if data_extended[i] == 1:
            for j in range(len(divisor)):
                data_extended[i + j] = xor(data_extended[i + j], divisor[j])
    return data + data_extended[-(len(divisor)-1):]