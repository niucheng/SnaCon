#!/usr/bin/env python
# coding: utf-8

# Welcome slogan
cli_slogan = 'Type "%shelp%s", "%scredits%s" for more information.' % ('%(INFO)s', '%(NORMAL)s', '%(INFO)s', '%(NORMAL)s')

# Prompt
PS1 = '> '

# Version
cli_version_short = '0.1.20140618.1'

# Help info
cli_help = """        COMMAND     DESCRIPTION
        ==============================
        CREDITS     Show the staff
        EXIT        Quit this program
        HELP        Display this page
        VERSION     License information"""
cli_credits = """Snake Console (SnaCon)
Hi there!
Yet another %sterminal emulator%s implemented using python the snake.""" % ('%(INFO)s', '%(NORMAL)s')
cli_version = '%sSnaCon%s  Ver ' % ('%(INFO)s', '%(NORMAL)s') + cli_version_short

# Error message
cli_invalid = '%sInvalid command%s' % ('%(ERROR)s', '%(NORMAL)s')

# Farewell
cli_farewell = '%sHave a lot of fun! %sBye%s' % ('%(INFO)s', '%(WARN)s', '%(NORMAL)s')

# Terminal
terminal_name_prefix = 'xterm'

# Terminal color
terminal_color_key_info = 'INFO'
terminal_color_key_warn = 'WARN'
terminal_color_key_error = 'ERROR'
terminal_color_key_normal = 'NORMAL'
terminal_color_key_success = 'SUCCESS'
#
terminal_color_set = {
    terminal_color_key_info    :  '\033[0;36m',
    terminal_color_key_warn    :  '\033[0;33m',
    terminal_color_key_error   :  '\033[0;31m',
    terminal_color_key_normal  :  '\x1B[0m',
    terminal_color_key_success :  '\x1B[1;36m'}
terminal_none_color_set = {
    terminal_color_key_info    :  '',
    terminal_color_key_warn    :  '',
    terminal_color_key_error   :  '',
    terminal_color_key_normal  :  '',
    terminal_color_key_success :  ''}

