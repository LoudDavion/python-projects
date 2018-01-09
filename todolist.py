"""
Command line to-do list program
"""

import sys
import os

# Catagories, can have sub catagories
# Items, simply lines of text
# add, command to add an item or catagory
# remove, command to delete an item or catagory
# quit, quit program
# list, shows the entire to do list
# organize, sort the items in alphabetical order
# open, opens a catagory
# leave, leaves a catagory

# Create the file if it not already there
if not os.path.isfile('userlist.txt'):
    with open('userlist.txt', 'w+') as ul:
        ul.write('\n')

def userhelp():
    print('-------------------------------\n'
          'open n to open catagory number n\n'
          'leave to get out of current catagory\n'
          'add item or add cat to add an item or catagory\n'
          'rm item n or rm cat n to remove the specified item or catagory\n'
          'list to show the entire to do list\n'
          'organize to sort in alphabetical order\n'
          'quit to exit program\n'
          '-------------------------------')

# Open file for editing
with open('userlist.txt', 'r+') as ul:
    print(ul.read())
    CURRENT_CAT = 0
    while True:
        USERIN = input("Enter a command (help, open, leave, add, remove, list, organize, quit): ")
        CATAGORIES = []
        INPUT_QUEUE = USERIN.split()
        UCOMMAND = INPUT_QUEUE[0]
        if 'help' in UCOMMAND:
            userhelp()
        elif 'open' in UCOMMAND:
            try:
                CURRENT_CAT = INPUT_QUEUE[1]
            except IndexError:
                print('invalid input, must input existing catagory number')
        elif 'leave' in UCOMMAND:
            CURRENT_CAT = 0
        elif 'add' in UCOMMAND:
            if 'catagory' in INPUT_QUEUE[1]:
                ul.write('-> {}\n'.format(INPUT_QUEUE[2]))
                ul.seek(0)
                print(ul.read())
            if 'item' in INPUT_QUEUE[1]:
                if CURRENT_CAT != 0:
                    ul.seek(int(CURRENT_CAT))
                    ul.write(' \n * {}'.format(' '.join(INPUT_QUEUE[2:])))
                    ul.seek(0)
                    print(ul.read())
                    ul.seek(int(CURRENT_CAT))
                else:
                    print("must open a catagory")
        elif 'remove' in UCOMMAND:
            pass
        elif 'list' in UCOMMAND:
            ul.seek(0)
            print(ul.read())
        elif 'organize' in UCOMMAND:
            pass
        elif 'quit' in UCOMMAND:
            sys.exit()
    sys.exit()
