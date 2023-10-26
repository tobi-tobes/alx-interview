#!/usr/bin/python3
"""
0-validate_utf8.py
Write a method that determines if a given data set
represents a valid UTF-8 encoding.

* Prototype: def validUTF8(data)
* Return: True if data is a valid UTF-8 encoding, else return False
* A character in UTF-8 can be 1 to 4 bytes long
* The data set can contain multiple characters
* The data will be represented by a list of integers
* Each integer represents 1 byte of data, therefore you only need to handle
  the 8 least significant bits of each integer
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    if type(data) is not list:
        return False
    if len(data) == 0:
        return False
    if len(data) == 1 and (data[0] > 127 or data[0] < 0):
        return False

    i = 0

    while i < len(data):
        if (data[i] & 0b10000000) == 0:
            i += 1
            continue
        elif (data[i] & 0b11100000) == 0b11000000:
            if i + 1 < len(data) and (data[i + 1] & 0b11000000) == 0b10000000:
                i += 2
            else:
                return False
        elif (data[i] & 0b11110000) == 0b11100000:
            for j in range(1, 3):
                if i + 2 > len(data) \
                        or (data[i + j] & 0b11000000) != 0b10000000:
                    return False
                else:
                    i += 3
        elif (data[i] & 0b11111000) == 0b11110000:
            for j in range(1, 4):
                if i + 3 > len(data) \
                        or (data[i + j] & 0b11000000) != 0b10000000:
                    return False
            else:
                i += 4
        else:
            return False

    return True
