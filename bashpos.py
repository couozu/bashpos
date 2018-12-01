#!/usr/bin/python

from __future__ import print_function
import sys
import readchar


def quit_terminal(c):
    print('Exiting...')
    sys.exit(0)


def help(c):
    global menu
    for i in menu.iteritems():
        print(' {} : {}'.format(i[0], i[1].description))


def unknown_command(c):
    print('Unknown command "{}". Available commands:'.format(c))
    help(c)


class Item:
    def __init__(self, handler, description):
        self.handler = handler
        self.description = description


unknown_command_item = Item(unknown_command, '')


def do_return_to_main():
    global menu
    global prompt
    menu = {
        'q': Item(quit_terminal, 'Exit from terminal'),
        'h': Item(help, 'Print context help'),
        'n': Item(new_check, 'New check')
    }
    prompt = ' > '


def return_to_main(c):
    do_return_to_main()
    print('Return to main menu')


def new_check(c):
    global menu
    global prompt
    menu = {
        'h': Item(help, 'Print context help'),
        'm': Item(return_to_main, 'Return to main menu')
    }
    print('Started new check')
    prompt = 'check > '


if __name__ == '__main__':
    print('Welcome to bashpos. Type "h" for help.')
    do_return_to_main()

    while True:
        print(prompt, end='')
        c = readchar.readchar()
        print(c)
        menu.get(c, unknown_command_item).handler(c)

