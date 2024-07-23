#!/usr/bin/python3
"""Module that defines a validUTF8 function."""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """return: True if all characters are utf8 valid, False otherwise"""
    bytes_to_check = 0

    for num in data:
        binary = format(num, '#010b')[-8:]

        if bytes_to_check == 0:
            if binary[0] == '0':
                continue
            elif binary.startswith('110'):
                bytes_to_check = 1
            elif binary.startswith('1110'):
                bytes_to_check = 2
            elif binary.startswith('11110'):
                bytes_to_check = 3
            else:
                return False
        else:
            if not binary.startswith('10'):
                return False
            bytes_to_check -= 1

    return bytes_to_check == 0
