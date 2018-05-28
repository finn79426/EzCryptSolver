#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from argparse import ArgumentParser
from Algorithm import *


if __name__ == "__main__":
    # argument processing
    parser = ArgumentParser(description="")
    parser.add_argument("-k", "--key", dest="key",
                        type=str, help="Specify FLAG Header")
    parser.add_argument("cipher")

    args = parser.parse_args()
    cipher = args.cipher
    key = args.key

    # Decoding
    Hexadecimal(cipher, key)
    Binary(cipher, key)
    Decimal(cipher, key)
    Base64(cipher, key)
    Base32(cipher, key)
    Urldecode(cipher, key)
    Reverse(cipher, key)
    Caesar_Cipher(cipher, key)
    Transposition_Cipher(cipher, key)
