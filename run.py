import sys
import time
import os

# Declare game variables
board = []

boardMap = []

for i in range(9):
    board.append("-")
    boardMap.append(i+1)

winner = None
game = True

# Welcome message with rules explained

def showRules():
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
        showRules()

""" 
Get player names and add 2 sec timer between 
name inputs
Player names get capitalised and must be letters
"""

def getPlayers():
    global playerX
    global playerO
    validNameX = None
    validNameO = None
    while not validNameX:
        time.sleep(0.2)
        playerX = input("Player x name: ").capitalize()
        try:
            if not playerX.isalpha():
                raise ValueError
            else:
                validNameX = True
                break
        except ValueError:
            print("Not X Valid name")
        print(playerX)
    while not validNameO:
        time.sleep(0.2)
        playerO = input("Player o name: ").capitalize()
        try:
            if not playerO.isalpha():
                raise ValueError
            else:
                validNameX = True
                break
        except ValueError:
            print("Not O Valid name")
        print(playerO)
    return playerX, playerO

# Playing board and map of the board

def viewBoard(board, boardMap):
    print("\n===========================================")
    print(f"""\nGame:            Map:
    {board[0]} | {board[1]} | {board[2]}        {boardMap[0]} | {boardMap[1]} | {boardMap[2]}
    __________        __________
    {board[3]} | {board[4]} | {board[5]}        {boardMap[3]} | {boardMap[4]} | {boardMap[5]}
    __________        __________
    {board[6]} | {board[7]} | {board[8]}        {boardMap[6]} | {boardMap[7]} | {boardMap[8]} """)

"""
Reads player X's input
Must be a number and must be between 1-9
"""

def readInputX(board, playerX):
    validMove = None
    while not validMove:
        try:
            pos = int(input(f"\n{playerX} go, please choose a position: "))
            if pos > 9 or pos == "":
                raise IndexError
            elif board[pos-1] != "-":
                raise ValueError
            else:
                board[pos-1] = "x"
                validMove = True
                break
        except ValueError:
            print("Invalid move, please choose a position on map")
        except IndexError:
            print("Invalid move, please pick a number between 1 - 9")

"""
Reads player O's input
Must be a number and must be between 1-9
"""

def readInputO(board, playerX):
    validMove = None
    while not validMove:
        try:
            pos = int(input(f"\n{playerX} go, please choose a position: "))
            if pos > 9 or pos == "":
                raise IndexError
            elif board[pos-1] != "-":
                raise ValueError
            else:
                board[pos-1] = "o"
                validMove = True
                break
        except ValueError:
            print("Invalid move, please choose a position on map")
        except IndexError:
            print("Invalid move, please pick a number between 1 - 9")

"""
Checks row for winner or draw
terminal is cleared of previous boards 
"""

def checkRow(board, playerX, playerO):
    global winner
    if board[0] == board[1] == board[2] != "-":
        if board[0] == "x":
            os.system('clear')
            print(f"\nWinner is {playerX}")
        elif board[0] == "o":
            os.system('clear')
            print(f"\nWinner is {playerO}")
        winner = True
    elif board[3] == board[4] == board[5] != "-":
        if board[3] == "x":
            os.system('clear')
            print(f"\nWinner is {playerX}")
        elif board[3] == "o":
            os.system('clear')
            print(f"\nWinner is {playerO}")
        winner = True
    elif board[6] == board[7] == board[8] != "-":
        if board[6] == "x":
            os.system('clear')
            print(f"\nWinner is {playerX}")
        elif board[6] == "o":
            os.system('clear')
            print(f"\nWinner is {playerO}")
        winner = True
    return winner         
    
"""
Checks column for winner or draw
terminal is cleared of previous boards 
"""

def checkColumn(board, playerX, playerO):
    global winner
    if board[0] == board[3] == board[6] != "-":
        if board[0] == "x":
            os.system('clear')
            print(f"\nWinner is {playerX}")
        elif board[0] == "o":
            os.system('clear')
            print(f"\nWinner is {playerO}")
        winner = True
    elif board[1] == board[4] == board[7] != "-":
        if board[1] == "x":
            os.system('clear')
            print(f"\nWinner is {playerX}")
        elif board[1] == "o":
            os.system('clear')
            print(f"\nWinner is {playerO}")
        winner = True
    elif board[2] == board[5] == board[8] != "-":
        if board[2] == "x":
            os.system('clear')
            print(f"\nWinner is {playerX}")
        elif board[2] == "o":
            os.system('clear')
            print(f"\nWinner is {playerO}")
        winner = True
    return winner

"""
Checks diagonal for winner or draw
terminal is cleared of previous boards 
"""
def checkDiagonal(board, playerX, playerO):
    global winner
    if board[0] == board[4] == board[8] != "-":
        if board[0] == "x":
            os.system('clear')
            print(f"\nWinner is {playerX}")
        elif board[0] == "o":
            os.system('clear')
            print(f"\nWinner is {playerO}")
        winner = True
    elif board[2] == board[4] == board[6] != "-":
        if board[2] == "x":
            os.system('clear')
            print(f"\nWinner is {playerX}")
        elif board[2] == "o":
            os.system('clear')
            print(f"\nWinner is {playerO}")
        winner = True
    return winner

"""
Checks for a winner or a draw
Asks user if they want to play again
Clears terminal if yes, exits if no
"""

def checkWin(board):
    global game
    global winner
    if winner:
        print("\nGAME OVER!!! See result below")
        time.sleep(0.5)
        viewBoard(board, boardMap)
        checkWin = input("\nWould you like to play again? Y/N ").lower()
        if checkWin =="y":
            game = True
            winner = False
            os.system('clear')
            for i in range(len(board)):
                board[i] = "-"
        elif checkWin =="n":
            sys.exit()
    elif "-" not in board:
        print("\nDRAW GAME See result below")
        time.sleep(0.5)
        viewBoard(board, boardMap)
        checkWin = input("\nWould you like to play again? Y/N ").lower()
        if checkWin =="y":
            game = True
            winner = False
            os.system('clear')
            for i in range(len(board)):
                board[i] = "-"
        elif checkWin =="n":
            sys.exit()
    return game, winner

# Main function to play game 

def main():
    showRules()
    getPlayers()
    viewBoard(board, boardMap)
    while game:
        readInputX(board, playerX) 
        viewBoard(board, boardMap)
        checkRow(board,playerX,playerO)
        checkColumn(board,playerX,playerO)
        checkDiagonal(board,playerX,playerO)
        checkWin(board)
        readInputO(board,playerO)
        viewBoard(board, boardMap)
        checkRow(board,playerX,playerO)
        checkColumn(board,playerX,playerO)
        checkDiagonal(board,playerX,playerO)
        checkWin(board)

main()
