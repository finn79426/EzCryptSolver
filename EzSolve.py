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
    parser = ArgumentParser()
    parser.add_argument("-k", "--key", dest="key",
                        type=str, help="Specify FLAG header")
    parser.add_argument("cipher")
    parser.add_argument("-l", help="Enable lone FLAG header list support", action='store_true') # Store Longlist flag
    args = parser.parse_args()


    cipher = args.cipher # Default

    # Processing the FLAG Header(key)
    if args.l:
        # Longlist mode ON
        with open("./FLAGList.txt") as fp:
            for oneline in fp:
                key = oneline.strip("\n")
                CrackEveryEncode(cipher, key) # Just centralize as one function
    else:
        # Just catch given key argument
        key = args.key
        CrackEveryEncode(cipher, key)
