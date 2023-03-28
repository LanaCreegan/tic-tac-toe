board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

boardMap = ["1", "2", "3", 
            "4", "5", "6",
            "7", "8", "9"]



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


def main():
    get_players()
    viewBoard(board, boardMap)
    readInputX(board, playerX)
main()
