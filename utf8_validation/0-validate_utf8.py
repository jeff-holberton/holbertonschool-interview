#!/usr/bin/python3
"""UTF-8 Validation Algorithm"""


def validUTF8(data):
    started = 0
    character_length = 0
    for n in data:
        if started == 0:
            binary_str = f"{n:08b}"
            if binary_str[0] == "0":
                return True
            elif binary_str[0] == "1" and binary_str[1] == "0":
                return False
            index = 0
            while binary_str[index] == "1":
                character_length += 1
                index += 1
            started = 1
        else:
            binary_str = f"{n:08b}"
            if binary_str[0] != "1" or binary_str[1] != "0":
                return False
            character_length -= 1
            if character_length == 0:
                started = 0
    return True
