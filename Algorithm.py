#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

import inspect
import urlparse
from base64 import b32decode
from AuthFlag import Key_Check


def CrackEveryEncode(cipher, key):
    Hexadecimal(cipher, key)
    Binary(cipher, key)
    Decimal(cipher, key)
    Base64(cipher, key)
    Base32(cipher, key)
    Urldecode(cipher, key)
    Reverse(cipher, key)
    Caesar_Cipher(cipher, key)
    Transposition_Cipher(cipher, key)


def Hexadecimal(cipher, key):
    decode = ""
    cipher = cipher.replace(" ", "")  # clean space
    try:
        decode = cipher.decode("hex")
    except TypeError:
        pass  # if TypeError, mean cipher has a word out of G-Z words

    # has key
    if key is not None:
        Key_Check(key, decode)
    else:
        name = inspect.stack()[0][3]  # function name
        print "{} : {}".format(name, decode)


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
    if key is not None:
        Key_Check(key, decode)
    else:
        name = inspect.stack()[0][3]  # function name
        print "{} : {}".format(name, decode)


def Decimal(cipher, key):
    decode = ""
    if " " not in cipher:
        pass  # if not had space, can't decode as Decimal
    else:
        try:
            cipher_list_int = cipher.split(" ")
            cipher_list_int = map(int, cipher_list_int)  # type = list&int
            decode = [chr(word) for word in cipher_list_int]  # type = list&str
            decode = "".join(decode)  # type = str
        except ValueError:
            pass  # if cipher is hex, pass

    # has key
    if key is not None:
        Key_Check(key, decode)
    else:
        name = inspect.stack()[0][3]  # function name
        print "{} : {}".format(name, decode)


def Base64(cipher, key):
    decode = ""
    try:
        decode = cipher.decode('base64')
    except:
        pass  # if any ERROR, mean cipher is not a Base64

    # has key
    if key is not None:
        Key_Check(key, decode)
    else:
        name = inspect.stack()[0][3]  # function name
        print "{} : {}".format(name, decode)


def Base32(cipher, key):
    decode = ""
    if " " in cipher:
        pass  # base32 do not allow space

    try:
        decode = b32decode(cipher)
    except:
        pass  # if any ERROR, mean cipher is not a Base32

    # has key
    if key is not None:
        Key_Check(key, decode)
    else:
        name = inspect.stack()[0][3]  # function name
        print "{} : {}".format(name, decode)


def Urldecode(cipher, key):
    decode = ''
    try:
        decode = urlparse.unquote(cipher)
    except:
        pass

    # has key
    if key is not None:
        Key_Check(key, decode)
    else:
        name = inspect.stack()[0][3]
        print "{} : {}".format(name, decode)


def Reverse(cipher, key):
    decode = cipher[::-1]

    # has key
    if key is not None:
        Key_Check(key, decode)
    else:
        name = inspect.stack()[0][3]  # function name
        print "{} : {}".format(name, decode)


def Caesar_Cipher(cipher, key):
    if key is not None:
        move = 1
        for x in range(26):
            decode = ""
            for c in cipher:
                if c.isalpha():
                    if c.isupper():
                        caps = True
                    else:
                        caps = False
                    alphabet = ord(c.lower()) + move
                    if alphabet > ord('z'):
                        alphabet -= 26
                    letter = chr(alphabet)
                    if caps is True:
                        letter = letter.upper()
                    decode += letter
                else:
                    decode += c

            Key_Check(key, decode)
            move += 1


def Transposition_Cipher(cipher, key):
    if key is not None:
        # 從切 2 開始
        for cut in range(1, len(cipher)-1):
            decode = ""
            count = 0
            for word in cipher:
                count += 1
                if count % cut == 0:
                    decode += word
            Key_Check(key, decode)
