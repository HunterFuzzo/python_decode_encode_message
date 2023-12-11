def ascii_to_binary(ascii_list):
    binary_string = ' '.join(format(code, '08b') for code in ascii_list).replace(" ", "")
    return [int(bit) for bit in binary_string]

def binary_to_ascii(binary_list):
    binary_values = binary_list.split()
    return ''.join(chr(int(binary, 2)) for binary in binary_values)