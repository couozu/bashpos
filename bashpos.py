#!/usr/bin/python

from __future__ import print_function
import sys
import readchar

#menu = {}
#prompt = {}

def unknown_command(c):
    print('Unknown command "{}". Type "h" for list available commands.'.format(c))


def quit_terminal(c):
    print('Exiting...')
    sys.exit(0)


def help(c):
    global menu
    for i in menu.iteritems():
        print(' {} : {}'.format(i[0], i[1].description))


class Item:
    def __init__(self, handler, description):
        self.handler = handler
        self.description = description


unknown_command_item = Item(unknown_command, '')

main_menu = {
    'q': Item(quit_terminal, 'Exit from terminal'),
    'h': Item(help, 'Print context help')
}

main_menu_prompt = '> '
menu = main_menu
prompt = main_menu_prompt

while True:
    print(prompt, end='')
    c = readchar.readchar()
    print(c)
    menu.get(c, unknown_command_item).handler(c)

