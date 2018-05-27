#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

import sys
import inspect
import pyperclip
from termcolor import cprint

def Key_Check(key, decode):
    if decode == "":
        pass
    else:
        if str(key) in decode:
            cprint("FLAG found !!!!!", "green")
            name = inspect.stack()[1][3]  # caller function name

            print "==========", name, "=========="
            cprint(decode, "magenta")
            print "==========", name, "=========="

            pyperclip.copy(decode)
            print "\nAlread copy to your clipboard. :)"
            sys.exit(0)
        else:
            pass
