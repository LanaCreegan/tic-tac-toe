""" Imported modules """
import sys
import time
import os

""" Declare game variables """
board = []
map = []

for i in range(9):
    board.append("-")
    map.append(i+1)

WINNER = None
GAME = True


def show_rules():
    """ Welcome message with rules explained, checks whether user understands
        rules
        checks for acknowledgement and starts game
    """
    understand = None
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

    while not understand:
        try:
            ack = input("Y/N: ").lower()
            if ack == "y":
                print("\nGreat the game will start in 3 seconds, get ready")
                time.sleep(3)
                os.system('clear')
                understand = True
                break
            elif ack == "n":
                print("Here are the rules again")
                time.sleep(1)
                print("\n")
                os.system('clear')
                show_rules()
                understand = True
                break
            else:
                understand = False
                raise ValueError
        except ValueError:
            print("Please enter 'Y' for yes and 'N' for no")


def get_players():
    """
    Gets player names
    Player names get capitalised and must be letters
    Verifies valid input
    """
    global player_x
    global player_o
    valid_name_x = None
    valid_name_o = None
    while not valid_name_x:
        time.sleep(0.2)
        player_x = input("\nPlayer X, please enter your name: ").capitalize()
        try:
            if not player_x.isalpha():
                raise ValueError
            else:
                valid_name_x = True
                print(f"Thanks {player_x}, you are using X!")
                break
        except ValueError:
            print("Player X name is not valid, please enter again")
    while not valid_name_o:
        time.sleep(0.2)
        player_o = input("\nPlayer O, please enter your name:  ").capitalize()
        try:
            if not player_o.isalpha():
                raise ValueError
            else:
                valid_name_x = True
                print(f"Thanks {player_o}, you are using O!")
                break
        except ValueError:
            print("Player O name is not valid, please enter again")
    return player_x, player_o


def view_board(board, map):
    """ Playing board and map of the board """
    print("\n")
    print(f"""\nMap:

    {map[0]} | {map[1]} | {map[2]}
    __________

    {map[3]} | {map[4]} | {map[5]}
    __________

    {map[6]} | {map[7]} | {map[8]}""")

    print(f"""\nGame:

    {board[0]} | {board[1]} | {board[2]}
    __________
    
    {board[3]} | {board[4]} | {board[5]}
    __________
    
    {board[6]} | {board[7]} | {board[8]}""")
    print("\n")


def read_input_x(board, player_x):
    """
    Reads player X's input
    Must be a number and must be between 1-9 and not empty
    """
    valid_move = None
    while not valid_move:
        try:
            pos = int(input(f"\n{player_x} go, please choose a position: "))
            if pos > 9 or pos == "" or pos == 0:
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


def read_input_o(board, player_o):
    """
    Reads player O's input
    Must be a number and must be between 1-9 and not empty
    """
    valid_move = None
    while not valid_move:
        try:
            pos = int(input(f"\n{player_o} go, please choose a position: "))
            if pos > 9 or pos == "" or pos == 0:
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


def check_row(board, player_x, player_o):
    """
    Checks row for winner, if winner is found
    terminal is cleared of previous boards
    """
    global WINNER
    if board[0] == board[1] == board[2] != "-":
        if board[0] == "x":
            os.system('clear')
            print(f"\nWinner is {player_x}")
        elif board[0] == "o":
            os.system('clear')
            print(f"\nWinner is {player_o}")
        WINNER = True
    elif board[3] == board[4] == board[5] != "-":
        if board[3] == "x":
            os.system('clear')
            print(f"\nWinner is {player_x}")
        elif board[3] == "o":
            os.system('clear')
            print(f"\nWinner is {player_o}")
        WINNER = True
    elif board[6] == board[7] == board[8] != "-":
        if board[6] == "x":
            os.system('clear')
            print(f"\nWinner is {player_x}")
        elif board[6] == "o":
            os.system('clear')
            print(f"\nWinner is {player_o}")
        WINNER = True
    return WINNER


def check_column(board, player_x, player_o):
    """
    Checks column for winner, if winner is found
    terminal is cleared of previous boards
    """
    global WINNER
    if board[0] == board[3] == board[6] != "-":
        if board[0] == "x":
            os.system('clear')
            print(f"\nWinner is {player_x}")
        elif board[0] == "o":
            os.system('clear')
            print(f"\nWinner is {player_o}")
        WINNER = True
    elif board[1] == board[4] == board[7] != "-":
        if board[1] == "x":
            os.system('clear')
            print(f"\nWinner is {player_x}")
        elif board[1] == "o":
            os.system('clear')
            print(f"\nWinner is {player_o}")
        WINNER = True
    elif board[2] == board[5] == board[8] != "-":
        if board[2] == "x":
            os.system('clear')
            print(f"\nWinner is {player_x}")
        elif board[2] == "o":
            os.system('clear')
            print(f"\nWinner is {player_o}")
        WINNER = True
    return WINNER


def check_diagonal(board, player_x, player_o):
    """
    Checks diagonal for winner, if winner is found
    terminal is cleared of previous boards
    """
    global WINNER
    if board[0] == board[4] == board[8] != "-":
        if board[0] == "x":
            os.system('clear')
            print(f"\nWinner is {player_x}")
        elif board[0] == "o":
            os.system('clear')
            print(f"\nWinner is {player_o}")
        WINNER = True
    elif board[2] == board[4] == board[6] != "-":
        if board[2] == "x":
            os.system('clear')
            print(f"\nWinner is {player_x}")
        elif board[2] == "o":
            os.system('clear')
            print(f"\nWinner is {player_o}")
        WINNER = True
    return WINNER


def check_win(board):
    """
    Checks for a WINNER or a draw
    Asks user if they want to play again
    clears terminal and resets game if yes, exits if no
    Checks for valid user input
    """
    global GAME
    global WINNER
    decision = None
    while not decision:
        try:
            if WINNER:
                print("\nGAME OVER!!! See result below: ")
                time.sleep(0.5)
                view_board(board, map)
                check_win = input("\nPlay again? Y/N: ").lower()
                if check_win == "y":
                    GAME = True
                    WINNER = False
                    os.system('clear')
                    for i in range(len(board)):
                        board[i] = "-"
                    decision = True
                elif check_win == "n":
                    sys.exit()
                else:
                    decision = False
                    raise ValueError
            elif "-" not in board:
                print("\nDRAW GAME!!! See result below: ")
                time.sleep(5)
                view_board(board, map)
                check_win = input("\nPlay again? Y/N: ").lower()
                if check_win == "y":
                    GAME = True
                    WINNER = False
                    os.system('clear')
                    for i in range(len(board)):
                        board[i] = "-"
                    decision = True
                elif check_win == "n":
                    sys.exit()
                else:
                    decision = False
                    raise ValueError
            return GAME, WINNER
        except ValueError:
            print("Please enter 'Y' for yes and 'N' for no")
            


def main():
    """ Main function to play game """
    show_rules()
    get_players()
    view_board(board, map)
    while GAME:
        read_input_x(board, player_x)
        view_board(board, map)
        check_row(board, player_x, player_o)
        check_column(board, player_x, player_o)
        check_diagonal(board, player_x, player_o)
        check_win(board)
        read_input_o(board, player_o)
        view_board(board, map)
        check_row(board, player_x, player_o)
        check_column(board, player_x, player_o)
        check_diagonal(board, player_x, player_o)
        check_win(board)


main()
