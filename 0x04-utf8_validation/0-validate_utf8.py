#!/usr/bin/python3
"""a function  that determines if a given data set represents a valid
   UTF-8 encoding. Return True if data is a valid UTF-8 encoding,
   else return False
"""


def set_bits_count(byte):
    """a function that counts the number of set bits (1)"""
    num = 0
    comparator = 1 << 7
    while comparator & byte:
        num += 1
        comparator = comparator >> 1
    return num


def validUTF8(data):
    """determines a valid UTF-8 encoding data set"""
    set_bits_num = 0
    for i in range(len(data)):
        if set_bits_num == 0:
            set_bits_num = set_bits_count(data[i])

            """checks 0xxxxxxx format"""
            if set_bits_num == 0:
                continue

            """a character in UTF-8 can be 1 to 4 bytes long"""
            if set_bits_num == 1 or set_bits_num > 4:
                return False
        else:
            """checks if current byte has no 00xxxxxx format"""
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        set_bits_num -= 1
    return set_bits_num == 0
