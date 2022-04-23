# Module Fungsi dan Prosedur Pendukung Program
# Kontributor : Enrique Alifio Ditya/16521253

from time import sleep

def loading(message):
# Fungsi menghasilkan animated loading message.
# KAMUS LOKAL
#   message : string
# ALGORITMA
    print(f"{message}", end="\r")
    sleep(0.25)
    print(f"{message}.",end="\r")
    sleep(0.25)
    print(f"{message}..",end="\r")
    sleep(0.25)
    print(f"{message}...",end="\r")
    print()

def replaceChar(word ,old, new):
# Fungsi mengganti suatu character (old) menjadi character baru (new) pada suatu string (word).
# KAMUS LOKAL
#   word, temp : string
#   old, new, character : character
# ALGORITMA
    temp = ""
    for character in word:
        if character != old:
            temp += character
        else:
            temp += new
    return temp     

def length(arr):
# Fungsi menghasilkan jumlah elemen pada arr, berfungsi seperti len() pada python 3.
# KAMUS LOKAL
#   total : integer
#   i : type element of array
#   arr : array
# ALGORITMA
    total = 0
    for i in arr:
        total += 1
    return total

def manualSplit(word, delimiter):
# Fungsi mengubah string menjadi elemen array yang dipisahkan oleh suatu character, berfungsi seperti fungsi split() di python 3.
# KAMUS LOKAL
# sumElement, idx, j : integer
# i, delimiter : character
# temp, word : string
# li : array of character
# ALGORITMA 
    sumElement = 1   # Counter element array setelah string terpisah
    for i in word:
        if i == delimiter:
            sumElement += 1
    li = [" " for i in range(sumElement)]
    temp = ""
    idx = 0
    j = 0
    for character in word:          # Proses pengisian array dari string yang terpisah karakter
        if character != delimiter:
            temp += character
            if j == length(word)-1:
                li[idx] = temp
        else:
            li[idx] = temp
            temp = ""
            idx += 1
        j += 1
    return li

def isWhitespace(word):
# Fungsi mengembalikan True apabila suatu string kosong atau spasi.
# Sering digunakan ketika mengecek apabila input string kosong.
# KAMUS LOKAL
#   empty : boolean
#   word : string
#   i : character
# ALGORITMA
    empty = True
    if length(word) == 0:
        return empty
    for i in word:
        if i != " ":
            empty = False
    return empty

def convertData(file):
# Fungsi ini mengonversi data pada file csv menjadi matrix.
# KAMUS LOKAL
    # f : SEQFILE
    # file, raw : string
    # arr : array of strings
    # matrix : matrix of strings
    # i : integer
# ALGORITMA
    f = open(file, "r")
    raw = f.readlines()
    f.close()
    arr = [replaceChar(line, "\n", "") for line in raw]
    matrix = [[] for i in range(length(arr))]
    i = 0
    for line in arr:
        matrix[i] = manualSplit(line, ";")
        i += 1
    return matrix  

def isInData(dataMatrix, element, column):
# Fungsi menghasilkan True apabila element terdapat di dalam kolom matriks tertentu.
# KAMUS LOKAL
#   found : boolean
#   line : array of strings
#   dataMatrix : matrix of strings
#   column : integer
# ALGORITMA
    found = False
    for line in dataMatrix:
        if line[column] == element:
            found = True
            break
    return found

def isInArr(e, arr):
# Fungsi mengembalikan True apabila elemen ada di dalam array.
# KAMUS LOKAL
#   ada : boolean
#   i : type element of array
# ALGORITMA
    ada = False
    for i in arr:
        if i == e:
            ada = True
            break
    return ada

def retrieveIdx(dataMatrix, element, column):
# Fungsi menghasilkan index matriks pertama kali elemen pada suatu kolom ditemukan.
# Prekondisi : elemen harus ada di dalam matriks.
# KAMUS LOKAL
#   dataMatrix : matrix of strings
#   element : string
#   i, column : integer
# ALGORITMA
    i = 0
    while element != dataMatrix[i][column] and i < (length(dataMatrix)-1):
        i += 1
    return i

def inputID(dataMtx):
# Prosedur melakukan validasi terhadap masukan ID.
# I.S dataMtx terdefinisi, F.S ID game terinput valid.
# KAMUS LOKAL
#   id : string
#   dataMtx : matrix of strings
# ALGORITMA
    id = input("Masukkan ID game: ").upper()
    while not isInData(dataMtx, id, 0) or isWhitespace(id):
        if isWhitespace(id):
            print()
            print("ID game tidak boleh kosong.")
        elif not isInData(dataMtx, id, 0):
            print()
            print("Tidak ada game dengan ID tersebut!")
        print()
        id = input("Masukkan ID game: ").upper()
    return id

def findLongestOnColumn(dataMtx, column):
# Fungsi menghasilkan panjang karakter string terpanjang dalam suatu kolom di matriks.
# Digunakan dalam proses menggambar tabel.
# KAMUS LOKAL
#   maxLen, i : integer
#   dataMtx : matrix of strings
# ALGORITMA
    maxLen = 0
    for i in range(length(dataMtx)):
        if length(dataMtx[i][column]) > maxLen:
            maxLen = length(dataMtx[i][column])
    return maxLen

def drawBorder(dataMtx):
# Prosedur menggambar border tabel matriks data.
# I.S dataMtx terdefinisi, F.S tergambar border tabel dataMtx.
# KAMUS LOKAL
#   sumLine, column, x : integer
#   dataMtx : matrix of strings
# ALGORITMA
    sumLine = 0
    column = length(dataMtx[0])
    for x in range(column):
        sumLine += findLongestOnColumn(dataMtx, x)
    sumLine += 2*column + column
    if length(dataMtx) >= 10:
        sumLine += 5
    else:
        sumLine += 4
    print("+", end="")
    print("-"*sumLine, end="")
    print("+")

def drawTable(dataMtx):
# Prosedur menggambar matriks data dalam bentuk tabel.
# I.S dataMtx terdefinisi, F.S tabel dataMtx tergambar.
# Prekondisi : Tabel harus memuat header.
# KAMUS LOKAL
#   i, maxLenColumn : integer
#   element : string
#   dataMtx : matrix of strings
# ALGORITMA
    drawBorder(dataMtx)
    if length(dataMtx) < 10:
        print("| No", end="")
    else:
        print("| No", end=" ")
    for i in range(length(dataMtx[0])):
        space = findLongestOnColumn(dataMtx, i) + 2 - length(dataMtx[0][i])
        if (space % 2) == 0:
            print(" | " + " "*(space//2-1) + replaceChar(str(dataMtx[0][i]).upper(), "_", " ") + " "*(space//2-1), end="")
        else:
            print(" | " + " "*(space//2-1) + replaceChar(str(dataMtx[0][i]).upper(), "_", " ") + " "*(space//2), end="")
    print(" |")
    drawBorder(dataMtx)

    for i in range(1, length(dataMtx)):
        if length(dataMtx) >= 100:
            if i >= 100:
                print("| " + str(i) + ".", end=" |")
            elif i >= 10 and i < 100:
                print("| " + str(i) + ".", end="  |")
            else:
                print("| " + str(i) + ".", end="   |")
        elif length(dataMtx) >= 10:
            if i >= 10 and i < 100:
                print("| " + str(i) + ".", end=" |")
            else:
                print("| " + str(i) + ".", end="  |")
        else:
            print("| " + str(i) + ".", end=" |")

        for j in range(length(dataMtx[i])):
            maxLenColumn = findLongestOnColumn(dataMtx, j)
            element = " " + str(dataMtx[i][j]) + " "*(maxLenColumn-length(dataMtx[i][j])) + " |"
            if j == (length(dataMtx[i])-1):
                print(element)
            else:
                print(element, end="")
    drawBorder(dataMtx)

def sortMtxCol(dataMtx, column, mode):
# Fungsi menghasilkan matriks yang terurut kolomnya sesuai mode.
# Mode 0 untuk ascending, mode selain 0 untuk descending.
# KAMUS LOKAL
#   sorted, dataMtx : matrix of strings
#   item : string
#   line : array of strings
#   mode, i, j : integer
# ALGORITMA
    sorted = [[item for item in line] for line in dataMtx]
    for i in range(1, length(sorted)):
        for j in range(1, length(sorted)):
            if mode == 0:
                if int(sorted[i][column]) < int(sorted[j][column]):
                    sorted[i], sorted[j] = sorted[j], sorted[i]
            else:
                if int(sorted[i][column]) > int(sorted[j][column]):
                    sorted[i], sorted[j] = sorted[j], sorted[i]
    return sorted

def hasGame(toko, kepemilikan, userID):
# Fungsi mengembalikan kumpulan game ID yang dimiliki oleh suatu user
# KAMUS LOKAL
#   jumlahGameDimiliki, idxGameDimiliki : integer
#   toko, kepemilikan : matrix of strings
#   line, IDGameDimiliki, g, game : array of strings
#   userID : string
# ALGORITMA
    jumlahGameDimiliki = 0
    for line in kepemilikan:
        if line[1] == userID:
            jumlahGameDimiliki += 1 
    IDgameDimiliki = [" " for i in range(jumlahGameDimiliki)]
    idxGameDimiliki = 0
    for line in kepemilikan:
        if line[1] == userID:
            IDgameDimiliki[idxGameDimiliki] = line[0]
            idxGameDimiliki += 1
    gameDimiliki = [" " for i in range(jumlahGameDimiliki)]
    idxGameDimiliki = 0
    for game in toko:
        if isInArr(game[0], IDgameDimiliki):
            g = [" " for i in range (length(game)-1)]
            for i in range(length(game)-1):
                g[i] = game[i]
            gameDimiliki[idxGameDimiliki] = g
            idxGameDimiliki += 1
    return gameDimiliki
