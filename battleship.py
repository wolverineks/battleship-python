from random import randint
import time
import os

def clear_screen():
    os.system('clear')

def layout():
    clear_screen()
    print""
    print""
    display_logo()
    display_title()
    print""
    print""

def welcome():
    layout()

def display_logo():

    print "                                    |__"
    print "                                    |\/"
    print "                                    ---"
    print "                                     / | ["
    print "                              !      | |||"
    print "                            _/|     _/|-++'"
    print "                        +  +--|    |--|--|_ |-"
    print "                     { /|__|  |/\__|  |--- |||__/"
    print "                    +---------------___[}-_===_.'____                   "
    print "                ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _"
    print " __..._____--==/___]_|__|_____________________________[___\==--____,------' .7"
    print "|                                                                     BB-61/"
    print " \_________________________________________________________________________|"

def display_title():

    print "  ___       __   _______   ___       ________  ________  _____ ______   _______           _________  ________      "
    print " |\  \     |\  \|\  ___ \ |\  \     |\   ____\|\   __  \|\    _   _   \|\   ___ \        |\___   __\/\   __  \     "
    print " \ \  \    \ \  \ \   __/|\ \  \    \ \  \___|\ \  \|\  \ \  \ \__\ \  \ \   __/|        \|___ \  \_\ \  \|\  \    "
    print "  \ \  \  __\ \  \ \  \_|/_\ \  \    \ \  \    \ \  \ \  \ \  \|__|  \  \ \  \_|/__           \ \  \ \ \  \ \  \   "
    print "   \ \  \|\__\_\  \ \  \_|\ \ \  \____\ \  \____\ \  \_\  \ \  \    \ \  \ \  \_|\ \           \ \  \ \ \  \_\  \  "
    print "    \ \____________\ \_______\ \_______\ \_______\ \_______\ \__\    \ \__\ \_______\           \ \__\ \ \_______\ "
    print "     \|____________|\|_______|\|_______|\|_______|\|_______|\|__|     \|__|\|_______|            \|__|  \|_______| "
    print "  ________  ________  _________  _________  ___       _______   ________  ___  ___  ___  ________    "
    print " |\   __  \|\   __  \|\___   ___\ ___   ___ \  \     |\  ___ \ |\   ____\|\  \|\  \|\  \|\   __  \   "
    print " \ \  \|\ /\ \  \|\  \|___ \  \_\|___ \  \_\ \  \    \ \   _ / \ \  \___|\ \  \_\  \ \  \ \  \|\  \  "
    print "  \ \   __  \ \   __  \   \ \  \     \ \  \ \ \  \    \ \  \_/ _\ \_____  \ \   __  \ \  \ \   ____\ "
    print "   \ \  \|\  \ \  \ \  \   \ \  \     \ \  \ \ \  \____\ \  \_|\ \|____|\  \ \  \ \  \ \  \ \  \___| "
    print "    \ \_______\ \__\ \__\   \ \__\     \ \__\ \ \_______\ \_______\____\_\  \ \__\ \__\ \__\ \__\    "
    print "     \|_______|\|__|\|__|    \|__|      \|__|  \|_______|\|_______|\_________\|__|\|__|\|__|\|__|    "
    print "                                                                   \|_________|                      "

def create_board():
    global board
    global turns
    global num
    board = []
    num = int(raw_input("How big would you like the board?: "))
    turns = num
    for x in range(0, num):
        board.append(["O"] * num)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def place_ship():
    global ship_row
    global ship_col
    ship_row = random_row(board)
    ship_col = random_col(board)

def print_board():
    global turns
    for row in board:
        print " ".join(row)
    print "--" * num
    print "Torpedos Left: %s" % (turns)

def get_guess():
    global turns
    global guess_row
    global guess_col

    if turns > 0:
      guess_row = int(raw_input("Guess Row: "))
      guess_col = int(raw_input("Guess Col: "))
      turns -= 1
    else: 
      print "***GAME OVER***"
      exit()

def debug(ship_row, ship_col):
    print "Row: %s, Column: %s" % (ship_row, ship_col)

def hit_or_miss(guess_row, guess_col):
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sank my battleship!"
    else:
        print_board()
        turn()
        print "You missed my battleship!"
        print "Guess again"

def turn():

    layout()

    print_board()
    
    debug(ship_row, ship_col)
      
    get_guess()  

    hit_or_miss(guess_row, guess_col)

def game():

    welcome()

    create_board()

    place_ship()

    turn()

game()