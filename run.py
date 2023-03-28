board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

boardMap = ["1", "2", "3", 
            "4", "5", "6",
            "7", "8", "9"]

winner = None

# get player names
def get_players():
    global playerX
    global playerO
    playerX = input("Player X name: ")
    playerO = input("PLayer O name: ")
    return playerX, playerO

def viewBoard(board, boardMap):
    print("\n===========================================")
    print(f"""\nGame:            Map:
    {board[0]} | {board[1]} | {board[2]}        {boardMap[0]} | {boardMap[1]} | {boardMap[2]}
    __________        __________
    {board[3]} | {board[4]} | {board[5]}        {boardMap[3]} | {boardMap[4]} | {boardMap[5]}
    __________        __________
    {board[6]} | {board[7]} | {board[8]}        {boardMap[6]} | {boardMap[7]} | {boardMap[8]} """)


def readInputX(board, playerX):
    pos = int(input(f"\n{playerX} poistion: "))
    board[pos-1] = "x"
    viewBoard(board, boardMap)

def readInputO(board, playerO):
    pos = int(input(f"\n{playerO} position: "))
    board[pos-1] = "o"
    viewBoard(board, boardMap)

def checkRow(board, playerX, playerO):
    global winner
    if board[0] == board[1] == board[2] != "-":
        if board[0] == "x":
            print(f"\nWinner is {playerX}")
        elif board[0] == "o":
            print(f"\nWinner is {playerO}")
        winner = True
    elif board[3] == board[4] == board[5] != "-":
        if board[3] == "x":
            print(f"\nWinner is {playerX}")
        elif board[3] == "o":
            print(f"\nWinner is {playerO}")
        winner = True
    elif board[6] == board[7] == board[8] != "-":
        if board[6] == "x":
            print(f"\nWinner is {playerX}")
        elif board[6] == "o":
            print(f"\nWinner is {playerO}")
        winner = True
    return winner           
    
def checkColumn(board, playerX, playerO):
    global winner
    if board[0] == board[3] == board[6] != "-":
        if board[0] == "x":
            print(f"\nWinner is {playerX}")
        elif board[0] == "o":
            print(f"\nWinner is {playerO}")
        winner = True
    elif board[1] == board[4] == board[7] != "-":
        if board[1] == "x":
            print(f"\nWinner is {playerX}")
        elif board[1] == "o":
            print(f"\nWinner is {playerO}")
        winner = True
    elif board[2] == board[5] == board[8] != "-":
        if board[2] == "x":
            print(f"\nWinner is {playerX}")
        elif board[2] == "o":
            print(f"\nWinner is {playerO}")
        winner = True
    return winner

def checkDiagonal(board,playerX,playerO):
    global winner
    if board[0] == board[4] == board[8] != "-":
        if board[0] == "x":
            print(f"\nWinner is {playerX}")
        elif board[0] == "o":
            print(f"\nWinner is {playerO}")
        winner = True
    elif board[2] == board[4] == board[6] != "-":
        if board[2] == "x":
            print(f"\nWinner is {playerX}")
        elif board[2] == "o":
            print(f"\nWinner is {playerO}")
        winner = True
    return winner

def checkWin(board):
    if winner:
        viewBoard(board, boardMap)
        print("\nGame Over")
    else:
        print("\nNo Winner")


def main():
    get_players()
    while 1:
        viewBoard(board, boardMap)
        readInputX(board, playerX)
        readInputO(board, playerO)
        checkRow(board, playerX, playerO)
        checkColumn(board, playerX, playerO)
        checkDiagonal(board, playerX, playerO)
        checkWin(board)
main()
