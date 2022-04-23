# File Bonus Tic Tac Toe
# Kontributor : Enrique Alifio Ditya/16521253

import functions as func

def fullBoard(board):
# Fungsi menghasilkan True apabila papan telah terisi penuh.
# KAMUS LOKAL
#   full : boolean
#   row : array of character
#   character : character
#   board : matrix of character
# ALGORITMA
    full = True
    for row in board:
        for character in row:
            if character == "#":
                full = False
                return full
    return full

def win(board, player):
# Fungsi menghasilkan True apabila pemain telah menang serta state kemenangannya.
# KAMUS LOKAL
#   i, j : integer
#   won : integer
#   board : matrix of character
#   player : character
# ALGORTIMA
    # Cek kemenangan secara horizontal
    for i in range(3):
        won = True
        for j in range(3):
            if board[i][j] != player:
                won = False
                break
        if won : return (won,"horizontal.")

    # Cek kemenangan secara vertikal
    for i in range(3):
        won = True
        for j in range(3):
            if board[j][i] != player:
                won = False
                break
        if won : return (won,"vertikal.")
    won = True

    # Cek kemenangan secara diagonal kiri-atas ke kanan-bawah
    for i in range(3):
        if board[i][i] != player:
            won = False
            break
    if won : return (won,"diagonal.")
    won = True

    # Cek kemenangan secara diagonal kanan-atas ke kiri-bawah
    for i in range(3):
        if board[i][2-i] != player:
            won = False
            break
    if won : return (won,"diagonal.")
    else : return (won,"")

def drawBoard(board):
# Prosedur menggambarkan papan tic tac toe
# I.S board terdefinisi, F.S board tergambar
# KAMUS LOKAL
#   i, j : integer
#   element : string
#   board : matrix of character
# ALGORITMA
    for i in range(3):
        print("+---+---+---+")
        print("|", end="")
        for j in range(3):
            element = " " + str(board[i][j]) + " |"
            if j == (func.length(board[i])-1):
                print(element)
            else:
                print(element, end="")
    print("+---+---+---+")

def tictactoe():
# Prosedur permainan tic tac toe
# I.S program utama berjalan, F.S fitur tic tac toe berjalan
# KAMUS LOKAL
#   board : matrix of characters
#   player : character
#   x, y : integer
# ALGORITMA
    board = [["#" for j in range(3)] for i in range(3)]
    player = "X"
    while not (win(board, "X")[0] or win(board, "O")[0] or fullBoard(board)):   # Program akan berjalan selama belum ada yang menang atau board belum penuh
        print()
        drawBoard(board)
        print()
        print("Giliran pemain " + player + ".")
        x = int(input("Baris : "))-1
        y = int(input("Kolom : "))-1
        while (x < 0) or (x > 2) or (y < 0) or (y > 2) or (board[x][y] != "#"): # Validasi masukan
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
