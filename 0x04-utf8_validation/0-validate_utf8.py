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
        if data[i] in range(0, 128):
            i += 1
            continue
        elif data[i] in range(194, 224):
            try:
                if data[i + 1] not in range(128, 192):
                    return False
            except Exception:
                return False
            i += 2
            continue
        elif data[i] in range(224, 240):
            try:
                for j in range(0, 2):
                    if data[i + j] not in range(128, 192):
                        return False
            except Exception:
                return False
            i += 3
            continue
        elif data[i] in range(240, 248):
            try:
                for j in range(0, 3):
                    if data[i + j] not in range(128, 192):
                        return False
            except Exception:
                return False
            i += 4
            continue
        else:
            return False

    return True
