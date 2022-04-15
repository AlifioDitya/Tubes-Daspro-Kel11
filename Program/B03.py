import functions as func

def fullBoard(board):
# Fungsi mengecek apabila papan telah terisi penuh.
    full = True
    for row in board:
        if "#" in row:
            full = False
    return full

def win(board, player):
# Fungsi mengecek apabila pemain telah menang dan state kemenangannya.
    for i in range(3):
        won = True
        for j in range(3):
            if board[i][j] != player:
                won = False
                break
        if won : return (won,"horizontal.")
    for i in range(3):
        won = True
        for j in range(3):
            if board[j][i] != player:
                won = False
                break
        if won : return (won,"vertikal.")
    won = True
    for i in range(3):
        if board[i][i] != player:
            won = False
            break
    if won : return (won,"diagonal.")
    won = True
    for i in range(3):
        if board[i][2-i] != player:
            won = False
            break
    if won : return (won,"diagonal.")
    else : return (won,"")

def drawBoard(board):
# Prosedur menggambarkan papan tic tac toe
    for i in range(3):
        print("+---+---+---+")
        print("|", end="")
        for j in range(3):
            maxLenColumn = func.findLongestOnColumn(board, j)
            element = " " + str(board[i][j]) + " |"
            if j == (func.length(board[i])-1):
                print(element)
            else:
                print(element, end="")
    print("+---+---+---+")

def tictactoe():
# Prosedur permainan tic tac toe
    board = [["#" for j in range(3)] for i in range(3)]
    player = "X"
    while not (win(board, "X")[0] or win(board, "O")[0] or fullBoard(board)):
        print()
        drawBoard(board)
        print()
        print("Giliran pemain " + player + ".")
        x = int(input("Baris : "))-1
        y = int(input("Kolom : "))-1
        while (x < 0) or (x > 2) or (y < 0) or (y > 2) or (board[x][y] != "#"):
            print()
            if (x < 0) or (x > 2) or (y < 0) or (y > 2):
                print("Mohon input pada rentang [1..3].")
            elif (board[x][y] != "#"):
                print("Posisi sudah terisi.")
            print()
            drawBoard(board)
            print()
            print("Giliran pemain " + player + ".")
            x = int(input("Baris : "))-1
            y = int(input("Kolom : "))-1
        board[x][y] = player
        if win(board, player)[0]:
            print()
            drawBoard(board)
            print()
            print(player, "menang secara", win(board, player)[1])
        elif fullBoard(board):
            print()
            drawBoard(board)
            print()
            print("Seri, tidak ada yang menang.")
        if player == "X":
            player = "O"
        else:
            player = "X"
