import sys
import time
import os

# Declare game variables
board = []

board_map = []

for i in range(9):
    board.append("-")
    board_map.append(i+1)

winner = None
game = True

# Welcome message with rules explained


def show_rules():
    print("""
    Welcome to Tic Tac Toe. The rules are simple: \n
    - User one will be asked to enter their name to use 'X'
    - User two will be asked to enter their name to use 'O'
    - The game displays on a 3 x 3 grid, along with a map
    - Using numbers 1-9, put your symbol in an empty slot
    - When 3 spots have been filled horizontally, diagonally
      or vertically, that person wins
    - If no one can fill three spots in a row the game is a draw \n
    Do you understand the rules?

    """)
    ack = input("Y/N: ").lower()
    if ack == "y":
        print("\nGreat the game will start in 3 seconds, get ready")
        time.sleep(3)
        os.system('clear')
    elif ack == "n":
        print("\nHere are the rules again")
        time.sleep(1)
        print("\n")
        show_rules()


"""
Get player names and add 2 sec timer between
name inputs
Player names get capitalised and must be letters
"""


def get_players():
    global player_x
    global player_o
    valid_name_x = None
    valid_name_o = None
    while not valid_name_x:
        time.sleep(0.2)
        player_x = input("Player x name: ").capitalize()
        try:
            if not player_x.isalpha():
                raise ValueError
            else:
                valid_name_x = True
                break
        except ValueError:
            print("Not X Valid name")
        print(player_x)
    while not valid_name_o:
        time.sleep(0.2)
        player_o = input("Player o name: ").capitalize()
        try:
            if not player_o.isalpha():
                raise ValueError
            else:
                valid_name_x = True
                break
        except ValueError:
            print("Not O Valid name")
        print(player_o)
    return player_x, player_o


# Playing board and map of the board


def view_board(board, board_map):
   
    print(f"""\nMap:            

    {board_map[0]} | {board_map[1]} | {board_map[2]}
    __________

    {board_map[3]} | {board_map[4]} | {board_map[5]}
    __________

    {board_map[6]} | {board_map[7]} | {board_map[8]}""")

    print(f"""\nGame:            

    {board[0]} | {board[1]} | {board[2]}
    __________

    {board[3]} | {board[4]} | {board[5]}
    __________

    {board[6]} | {board[7]} | {board[8]}""")


"""
Reads player X's input
Must be a number and must be between 1-9
"""


def read_input_x(board, player_x):
    valid_move = None
    while not valid_move:
        try:
            pos = int(input(f"\n{player_x} go, please choose a position: "))
            if pos > 9 or pos == "":
                raise IndexError
            elif board[pos-1] != "-":
                raise ValueError
            else:
                board[pos-1] = "x"
                valid_move = True
                break
        except ValueError:
            print("Invalid move, please choose a position on map")
        except IndexError:
            print("Invalid move, please pick a number between 1 - 9")


"""
Reads player O's input
Must be a number and must be between 1-9
"""


def read_input_o(board, player_x):
    valid_move = None
    while not valid_move:
        try:
            pos = int(input(f"\n{player_x} go, please choose a position: "))
            if pos > 9 or pos == "":
                raise IndexError
            elif board[pos-1] != "-":
                raise ValueError
            else:
                board[pos-1] = "o"
                valid_move = True
                break
        except ValueError:
            print("Invalid move, please choose a position on map")
        except IndexError:
            print("Invalid move, please pick a number between 1 - 9")


"""
Checks row for winner or draw
terminal is cleared of previous boards
"""


def check_row(board, player_x, player_o):
    global winner
    if board[0] == board[1] == board[2] != "-":
        if board[0] == "x":
            os.system('clear')
            print(f"\nWinner is {player_x}")
        elif board[0] == "o":
            os.system('clear')
            print(f"\nWinner is {player_o}")
        winner = True
    elif board[3] == board[4] == board[5] != "-":
        if board[3] == "x":
            os.system('clear')
            print(f"\nWinner is {player_x}")
        elif board[3] == "o":
            os.system('clear')
            print(f"\nWinner is {player_o}")
        winner = True
    elif board[6] == board[7] == board[8] != "-":
        if board[6] == "x":
            os.system('clear')
            print(f"\nWinner is {player_x}")
        elif board[6] == "o":
            os.system('clear')
            print(f"\nWinner is {player_o}")
        winner = True
    return winner


"""
Checks column for winner or draw
terminal is cleared of previous boards
"""


def check_column(board, player_x, player_o):
    global winner
    if board[0] == board[3] == board[6] != "-":
        if board[0] == "x":
            os.system('clear')
            print(f"\nWinner is {player_x}")
        elif board[0] == "o":
            os.system('clear')
            print(f"\nWinner is {player_o}")
        winner = True
    elif board[1] == board[4] == board[7] != "-":
        if board[1] == "x":
            os.system('clear')
            print(f"\nWinner is {player_x}")
        elif board[1] == "o":
            os.system('clear')
            print(f"\nWinner is {player_o}")
        winner = True
    elif board[2] == board[5] == board[8] != "-":
        if board[2] == "x":
            os.system('clear')
            print(f"\nWinner is {player_x}")
        elif board[2] == "o":
            os.system('clear')
            print(f"\nWinner is {player_o}")
        winner = True
    return winner


"""
Checks diagonal for winner or draw
terminal is cleared of previous boards
"""


def check_diagonal(board, player_x, player_o):
    global winner
    if board[0] == board[4] == board[8] != "-":
        if board[0] == "x":
            os.system('clear')
            print(f"\nWinner is {player_x}")
        elif board[0] == "o":
            os.system('clear')
            print(f"\nWinner is {player_o}")
        winner = True
    elif board[2] == board[4] == board[6] != "-":
        if board[2] == "x":
            os.system('clear')
            print(f"\nWinner is {player_x}")
        elif board[2] == "o":
            os.system('clear')
            print(f"\nWinner is {player_o}")
    return winner


"""
Checks for a winner or a draw
Asks user if they want to play again
Clears terminal if yes, exits if no
"""


def check_win(board):
    global game
    global winner
    if winner:
        print("\nGAME OVER!!! See result below")
        time.sleep(0.5)
        view_board(board, board_map)
        check_win = input("\nWould you like to play again? Y/N ").lower()
        if check_win == "y":
            game = True
            winner = False
            os.system('clear')
            for i in range(len(board)):
                board[i] = "-"
        elif check_win == "n":
            sys.exit()
    elif "-" not in board:
        print("\nDRAW GAME See result below")
        time.sleep(0.5)
        view_board(board, board_map)
        check_win = input("\nWould you like to play again? Y/N ").lower()
        if check_win == "y":
            game = True
            winner = False
            os.system('clear')
            for i in range(len(board)):
                board[i] = "-"
        elif check_win == "n":
            sys.exit()
    return game, winner


# Main function to play game


def main():
    show_rules()
    get_players()
    view_board(board, board_map)
    while game:
        read_input_x(board, player_x)
        view_board(board, board_map)
        check_row(board, player_x, player_o)
        check_column(board, player_x, player_o)
        check_diagonal(board, player_x, player_o)
        check_win(board)
        read_input_o(board, player_o)
        view_board(board, board_map)
        check_row(board, player_x, player_o)
        check_column(board, player_x, player_o)
        check_diagonal(board, player_x, player_o)
        check_win(board)


main()
