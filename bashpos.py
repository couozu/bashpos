#!/usr/bin/python

from __future__ import print_function
import sys
import readchar


def unknown_command(c):
    print('Unknown command "{}". Type "h" for list available commands.'.format(c))


def quit(c):
    print('Exiting...')
    sys.exit(0)


main_menu = {
    'q': quit
}

main_menu_prompt = '> '

menu = main_menu
prompt = main_menu_prompt

while True:
    print(prompt, end='')
    c = readchar.readchar()
    print(c)
    menu.get(c, unknown_command)(c)

