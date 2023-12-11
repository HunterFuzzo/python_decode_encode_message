def crc_to_manchester(binary_list):
    return [1 if bit == 0 else 0 for bit in binary_list]


def manchester_to_crc(manchester_list):
    return [1 if bit == 0 else 0 for bit in manchester_list]