#!/usr/bin/env python
# coding: utf-8

import os

import Constant as constant

terminal_color_en = False

def check_env():
    global terminal_color_en
    #
    if os.environ.get('TERM')[:len(constant.terminal_name_prefix)] == constant.terminal_name_prefix:
        terminal_color_en = True

def puts(string):
    if terminal_color_en:
        print (string % constant.terminal_color_set)
    else:
        print (string % constant.terminal_none_color_set)

if __name__ == "__main__":
    puts('Before %scheck_env()%s (%s)' % ('%(INFO)s', '%(NORMAL)s', 'True' if terminal_color_en else 'False'))
    check_env()
    puts('After %scheck_env()%s (%s)' % ('%(INFO)s', '%(NORMAL)s', 'True' if terminal_color_en else 'False'))
    puts('[%sINFO%s][%sWARN%s][%sERROR%s][NORMAL][%sSUCCESS%s]' % ('%(INFO)s', '%(NORMAL)s', '%(WARN)s', '%(NORMAL)s', '%(ERROR)s', '%(NORMAL)s', '%(SUCCESS)s', '%(NORMAL)s'))

