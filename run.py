board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

boardmap = ["1", "2", "3", 
            "4", "5", "6",
            "7", "8", "9"]




def get_players():
    global playerX
    global playerO
    playerX = input("Player X name: ")
    playerO = input("PLayer O name: ")
    return playerX, playerO


get_players()


