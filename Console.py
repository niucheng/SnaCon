#!/bin/env python
# coding: utf-8

import os
import subprocess
import sys

import prog.Color as color
import prog.Constant as constant

if __name__ == "__main__":
    color.check_env()
    color.puts(constant.cli_slogan)

    while True:
        str_cmd = raw_input(constant.PS1)

        if str_cmd.strip().upper() == 'CREDITS':
            color.puts(constant.cli_credits)
            continue

        if str_cmd.strip().lower() == 'exit':
            break

        if str_cmd.strip().lower() == 'help':
            color.puts(constant.cli_help)
            continue

        if str_cmd.strip().lower() == 'version':
            color.puts(constant.cli_version)
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
                color.puts(line.rstrip())
            pass
        except OSError:
            color.puts(constant.cli_invalid)

        pass

    color.puts(constant.cli_farewell)

