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
from base64 import b32decode
# 如果 function 返回值(str)有包含 flag 開頭，即結束爆破


# Quick

def Hexadecimal(cipher, key):
    decode = ""
    cipher = cipher.replace(" ", "")  # clean space
    try:
        decode = cipher.decode("hex")
    except TypeError:
        pass # if TypeError, mean cipher has a word out of G-Z words

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
            sys.exit(0)
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
    try:
        for index in range(len(cipher)):
            if index+1 == 8:
                decode += chr(int(cipher[:index+1], 2))
            elif (index+1) % 8 == 0:
                decode += chr(int(cipher[index-7:index+1], 2))
    except ValueError:
        pass

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
            sys.exit(0)
        else:
            pass
    # no key
    else:
        name = inspect.stack()[0][3]  # function name
        print "==========", name, "=========="
        print decode
        print "==========", name, "==========\n"


def Decimal(cipher, key):
    decode = ""
    if " " not in cipher:
        pass  # if not had space, pass this algorithm
    else:
        try:
            cipher_list_int = cipher.split(" ")
            cipher_list_int = map(int, cipher_list_int)  # type = list&int
            decode = [chr(word) for word in cipher_list_int]  # type = list&str
            decode = "".join(decode)  # type = str
        except ValueError:
            pass # if cipher is hex, pass

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
            sys.exit(0)
        else:
            pass
    # no key
    else:
        name = inspect.stack()[0][3]  # function name
        print "==========", name, "=========="
        print decode
        print "==========", name, "==========\n"


def Base64(cipher, key):
    decode = ""
    if " " in cipher:
        pass # base64 do not allow space
    
    try:
        decode = cipher.decode('base64')
    except:
        pass # if any ERROR, mean cipher is not a Base64

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
            sys.exit(0)
        else:
            pass
    # no key
    else:
        name = inspect.stack()[0][3]  # function name
        print "==========", name, "=========="
        print decode
        print "==========", name, "==========\n"



def Base32(cipher, key):
    decode = ""
    if " " in cipher:
        pass # base32 do not allow space
    
    try:
        decode = b32decode(cipher)
    except:
        pass # if any ERROR, mean cipher is not a Base32

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
            sys.exit(0)
        else:
            pass
    # no key
    else:
        name = inspect.stack()[0][3]  # function name
        print "==========", name, "=========="
        print decode
        print "==========", name, "==========\n"

def Reverse(cipher, key):
    decode = cipher[::-1]
 
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
            sys.exit(0)
        else:
            pass
    # no key
    else:
        name = inspect.stack()[0][3]  # function name
        print "==========", name, "=========="
        print decode
        print "==========", name, "==========\n"
   

# def URLencode():

# def jsfuck():

# def aaencode():


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
    Decimal(cipher, key)
    Base64(cipher, key)
    Base32(cipher, key)
    Reverse(cipher, key)
