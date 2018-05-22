#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

import sys
import inspect
import pyperclip  # install
from argparse import ArgumentParser
from termcolor import colored, cprint  # install


# 如果 function 返回值(str)有包含 flag 開頭，即結束爆破


# Quick

def Hexadecimal(cipher, key):
    cipher = cipher.replace(" ", "")  # clean space
    decode = cipher.decode("hex")

    # has key
    if key != None:
        if str(key) in decode:
            cprint("FLAG found !!!!!", "green")
            name = inspect.stack()[0][3]  # function name
            print "==========", name, "=========="
            cprint(decode, "magenta")
            print "==========", name, "=========="

            pyperclip.copy(decode)
            print "\nAlread copy to your clipboard. :)"
        else:
            pass
    # no key
    else:
        name = inspect.stack()[0][3]  # function name
        print "==========", name, "=========="
        print decode
        print "==========", name, "==========\n"

def Binary(cipher, key):
    cipher = cipher.replace(" ", "")  # clean space
    decode = ""
    for index in range(len(cipher)):
        if index+1==8:
            decode +=  chr(int(cipher[:index+1], 2))
        elif (index+1)%8==0:
            decode +=  chr(int(cipher[index-7:index+1], 2))
    # has key
    if key != None:
        if str(key) in decode:
            cprint("FLAG found !!!!!", "green")
            name = inspect.stack()[0][3]  # function name
            print "==========", name, "=========="
            cprint(decode, "magenta")
            print "==========", name, "=========="

            pyperclip.copy(decode)
            print "\nAlread copy to your clipboard. :)"
        else:
            pass
    # no key
    else:
        name = inspect.stack()[0][3]  # function name
        print "==========", name, "=========="
        print decode
        print "==========", name, "==========\n"


# def Decimal():

# def Base64():

# def Base32():

# def URLencode():

# def jsfuck():

# def aaencode():

# def Reverse():

# Medium

# def Caesar_cipher():


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
    



