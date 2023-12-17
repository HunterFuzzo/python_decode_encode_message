def crc_to_manchester(binary_list):
    encoded_list = []
    for bit in binary_list:
        if bit == 0:
            encoded_list.extend([0, 1])  # '01'
        else:
            encoded_list.extend([1, 0])  # '10'
    return encoded_list