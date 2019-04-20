#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

import inspect
import urlparse
from HTMLParser import HTMLParser
from base64 import b32decode, b16decode
from base58 import b58decode
from quopri import decodestring
from AuthFlag import Key_Check


def CrackEveryEncode(cipher, key=None):
    # Encode transform
    Hexadecimal(cipher, key)
    Binary(cipher, key)
    Decimal(cipher, key)
    Base64(cipher, key)
    Base58(cipher, key)
    Base32(cipher, key)
    Base16(cipher, key)
    Urldecode(cipher, key)
    HTML_Entity(cipher, key)
    Quoted_printable(cipher, key)
    Reverse(cipher, key)
    # Brute force
    if key is not None:
        Caesar_Cipher(cipher, key)
        Transposition_Cipher(cipher, key)


def Hexadecimal(cipher, key=None):
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


def Binary(cipher, key=None):
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


def Decimal(cipher, key=None):
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


def Base64(cipher, key=None):
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


def Base58(cipher, key=None):
    decode = ""

    try:
        decode = b58decode(cipher)
    except:
        pass  # if any ERROR, mean cipher is not a Base58

    # has key
    if key is not None:
        Key_Check(key, decode)
    else:
        name = inspect.stack()[0][3]  # function name
        print "{} : {}".format(name, decode)


def Base32(cipher, key=None):
    decode = ""
    if " " in cipher:
        pass  # base32 not allow any whitespace

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


def Base16(cipher, key=None):
    decode = ""

    try:
        decode = b16decode(cipher)
    except:
        pass  # if any ERROR, mean cipher is not a Base16

    # has key
    if key is not None:
        Key_Check(key, decode)
    else:
        name = inspect.stack()[0][3]  # function name
        print "{} : {}".format(name, decode)


def Urldecode(cipher, key=None):
    decode = ""
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


def HTML_Entity(cipher, key=None):
    decode = ""
    try:
        decode = HTMLParser().unescape(cipher)
    except:
        pass

    # has key
    if key is not None:
        Key_Check(key, decode)
    else:
        name = inspect.stack()[0][3]
        print "{} : {}".format(name, decode.encode('utf-8'))


def Quoted_printable(cipher, key=None):
    decode = ""

    try:
        decode = decodestring(cipher)
    except:
        pass

    # has key
    if key is not None:
        Key_Check(key, decode)
    else:
        name = inspect.stack()[0][3]  # function name
        print "{} : {}".format(name, decode)


def Reverse(cipher, key=None):
    decode = cipher[::-1]

    # has key
    if key is not None:
        Key_Check(key, decode)
    else:
        name = inspect.stack()[0][3]  # function name
        print "{} : {}".format(name, decode)


def Caesar_Cipher(cipher, key):
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
    # 從切 2 開始
    for cut in range(1, len(cipher)-1):
        decode = ""
        count = 0
        for word in cipher:
            count += 1
            if count % cut == 0:
                decode += word
        Key_Check(key, decode)
