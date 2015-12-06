from random import randint
import time
import os

def clear_screen():
    os.system('clear')

def layout():
    clear_screen()
    print("")
    print("")
    display_logo()
    display_title()
    print("")
    print("")

# def welcome():
#     layout()

def display_logo():

    print("                                    |__")
    print("                                    |\/")
    print("                                    ---")
    print("                                     / | [")
    print("                              !      | |||")
    print("                            _/|     _/|-++'")
    print("                        +  +--|    |--|--|_ |-")
    print("                     { /|__|  |/\__|  |--- |||__/")
    print("                    +---------------___[}-_===_.'____                   ")
    print("                ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _")
    print(" __..._____--==/___]_|__|_____________________________[___\==--____,------' .7")
    print("|                                                                     BB-61/")
    print(" \_________________________________________________________________________|")

def display_title():

    print("  ___       __   _______   ___       ________  ________  _____ ______   _______           _________  ________      ")
    print(" |\  \     |\  \|\  ___ \ |\  \     |\   ____\|\   __  \|\    _   _   \|\   ___ \        |\___   __\/\   __  \     ")
    print(" \ \  \    \ \  \ \   __/|\ \  \    \ \  \___|\ \  \|\  \ \  \ \__\ \  \ \   __/|        \|___ \  \_\ \  \|\  \    ")
    print("  \ \  \  __\ \  \ \  \_|/_\ \  \    \ \  \    \ \  \ \  \ \  \|__|  \  \ \  \_|/__           \ \  \ \ \  \ \  \   ")
    print("   \ \  \|\__\_\  \ \  \_|\ \ \  \____\ \  \____\ \  \_\  \ \  \    \ \  \ \  \_|\ \           \ \  \ \ \  \_\  \  ")
    print("    \ \____________\ \_______\ \_______\ \_______\ \_______\ \__\    \ \__\ \_______\           \ \__\ \ \_______\ ")
    print("     \|____________|\|_______|\|_______|\|_______|\|_______|\|__|     \|__|\|_______|            \|__|  \|_______| ")
    print("  ________  ________  _________  _________  ___       _______   ________  ___  ___  ___  ________    ")
    print(" |\   __  \|\   __  \|\___   ___\ ___   __\|\  \     |\  ___ \ |\   ____\|\  \|\  \|\  \|\   __  \   ")
    print(" \ \  \|\ /\ \  \|\  \|___ \  \_\|___ \  \_\ \  \    \ \   _ / \ \  \___|\ \  \_\  \ \  \ \  \|\  \  ")
    print("  \ \   __  \ \   __  \   \ \  \     \ \  \ \ \  \    \ \  \_/ _\ \_____  \ \   __  \ \  \ \   ____\ ")
    print("   \ \  \|\  \ \  \ \  \   \ \  \     \ \  \ \ \  \____\ \  \_|\ \|____|\  \ \  \ \  \ \  \ \  \___| ")
    print("    \ \_______\ \__\ \__\   \ \__\     \ \__\ \ \_______\ \_______\____\_\  \ \__\ \__\ \__\ \__\    ")
    print("     \|_______|\|__|\|__|    \|__|      \|__|  \|_______|\|_______|\_________\|__|\|__|\|__|\|__|    ")
    print("                                                                   \|_________|                      ")

def choose_board_size():
    global board_size
    
    try:
      board_size = int(input("How big would you like the board?: "))
    except ValueError:
      layout()
      print"Please choose a number."
      choose_board_size()

def create_board():
    global board
    global turns
    board = []
    
    turns = board_size
    
    for x in range(0, board_size):
        board.append(["[]"] * board_size)

def random_row():
    return randint(0, len(board) - 1)

def random_col():
    return randint(0, len(board[0]) - 1)

def place_ship():
    global ship_row
    global ship_col
    ship_row = random_row()
    ship_col = random_col()

def printboard():
    global turns
    for row in board:
        print" ".join(row)
    print("***" * board_size)
    print("Torpedos Left: %s" % (turns))

def guess_sanitize():
    if guess_row not in range(board_size) or guess_col not in range(board_size):
        layout()
        printboard()
        print("Your torpedo has gone off the map!")

        get_guess()

def get_guess_row():
    global guess_row

    if turns > 0:
      try:
        user_row = int(input("Range: "))
        guess_row = board_size - user_row
      except ValueError:
        layout()
        printboard()
        print("Please choose a number.")
        get_guess_row()
    else: 
      print("***GAME OVER***")
      replay()

def get_guess_col():
    global guess_col

    try:
      user_col = int(input("Bearing: "))
      guess_col = user_col - 1
    except ValueError:
      layout()
      printboard()
      print("Please choose a number.")
      get_guess_col()

def get_guess():
    get_guess_row()
    get_guess_col()

def debug():
    print("Range: %s, Bearing: %s" % (ship_row, ship_col))

def decrement_turns():
    global turns
    turns -= 1

def hit_or_miss():
    guess_sanitize()

    if guess_col == ship_col and guess_row == ship_row: 
        print("Congratulations! You sank my battleship!")
        print("***GAME OVER***")
        replay()
    else:
        try:
            board[guess_row][guess_col] = " 0"
            printboard()
        except IndexError:
            print("Ship: Range: %s, Bearing: %s" % (ship_row, ship_col) )
            print("Guess: Range: %s, Bearing: %s" % (guess_row, guess_col) )

def turn():

    layout()

    printboard()
    
    debug()
      
    get_guess()

    decrement_turns()

    hit_or_miss()

    turn()

def replay():
    replay = input("Would you like to play again? (y/n) ")

    if replay == "y":
      game()
    else:
      exit()

def game():

    layout()

    choose_board_size()

    create_board()

    place_ship()

    turn()

game()