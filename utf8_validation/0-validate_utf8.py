#!/usr/bin/python3
"""UTF-8 Validation Algorithm"""


def validUTF8(data):
    """UTF-8 Validation Algorithm"""
    started = 0
    character_length = 0
    for n in data:
        eight_bits = n % 256
        binary_str = f"{eight_bits:08b}"
        if started == 0:
            if binary_str[0] == "0":
                continue
            elif binary_str[0] == "1" and binary_str[1] == "0":
                return False
            index = 1
            while binary_str[index] == "1":
                character_length += 1
                index += 1
            if character_length > 3:
                return False
            started = 1
        else:
            if n > 255 or n < 0:
                return False
            if binary_str[0] != "1" or binary_str[1] != "0":
                return False
            character_length -= 1
            if character_length == 0:
                started = 0
    if character_length != 0:
        return False
    return True
