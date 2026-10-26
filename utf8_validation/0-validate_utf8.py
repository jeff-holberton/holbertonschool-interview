#!/usr/bin/python3
"""UTF-8 Validation Algorithm"""


def validUTF8(data):
    started = 0
    character_length = 0
    for n in data:
        if n > 255 or n < 0:
            return False
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

if __name__ == "__main__":     
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))