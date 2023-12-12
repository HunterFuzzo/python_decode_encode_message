def ascii_to_binary(ascii_list):
    binary_string = ' '.join(format(code, '08b') for code in ascii_list).replace(" ", "")
    return [int(bit) for bit in binary_string]

def binary_to_ascii(binary_list):
    binary_string = ''.join(map(str, binary_list))
    chunks = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    ascii_list = [int(chunk, 2) for chunk in chunks]
    return ascii_list