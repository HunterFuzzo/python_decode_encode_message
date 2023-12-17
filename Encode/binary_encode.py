def ascii_to_binary(ascii_list):
    binary_string = ' '.join(format(code, '08b') for code in ascii_list).replace(" ", "")
    return [int(bit) for bit in binary_string]