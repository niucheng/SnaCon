#!/bin/env python
# coding: utf-8

import os
import subprocess
import sys

import prog.Constant as constant

print (constant.cli_slogan)

while True:
    str_cmd = raw_input(constant.PS1)

    if str_cmd.strip().upper() == 'CREDITS':
        print (constant.cli_credits)
        continue

    if str_cmd.strip().lower() == 'exit':
        break

    if str_cmd.strip().lower() == 'help':
        print (constant.cli_help)
        continue

    if str_cmd.strip().lower() == 'version':
        print (constant.cli_version)
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
        print (constant.cli_incalid)

    pass

