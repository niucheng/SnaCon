#!/bin/env python
# coding: utf-8

# http://stackoverflow.com/questions/7468668/python-subprocess-readlines

import os
import subprocess
import sys

print ('Type "help", "credits" for more information.')

while True:
    str_cmd = raw_input('> ')

    if str_cmd.strip().lower() == 'exit':
        break

    if str_cmd.strip().lower() == 'help':
        print ("""
        COMMAND    DESCRIPTION
        ==============================
        CREDITS    Show the sfaff
        EXIT       Quit this programe
        HELP       Display this page
               """)
        continue

    if str_cmd.strip().upper() == 'CREDITS':
        print ("""
        Hi there!
               """)
        continue

    #if str_cmd == '':
    #    continue

    try:
        proc = subprocess.Popen(str_cmd,
                                shell=True,
                                stdout=subprocess.PIPE,
                                #stderr=subprocess.PIPE,
                                universal_newlines=True)
        out, err = proc.communicate()
        for line in out.splitlines():
            print (line.rstrip())
        pass
    except OSError:
        print ('Invalid command')

    pass

