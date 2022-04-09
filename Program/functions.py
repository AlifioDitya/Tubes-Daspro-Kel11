# File ini memuat fungsi/prosedur pendukung program

def countRow(file):
# Fungsi ini menghitung jumlah baris pada file csv
    f = open(file, "r")
    row = 0
    for i in f:
        row += 1
    f.close()
    return row

def countColumn(file):
# Fungsi ini menghitung jumlah kolom pada file csv
# Prekondisi : file harus terisi setidaknya 1 elemen (termasuk header)
    f = open(file, "r")
    column = 1
    raw = [line for line in f]
    for i in raw[0]:
        if i == ";":
            column += 1
    f.close()
    return column

def replaceChar(word ,old, new):
# fungsi mengganti suatu character (old) menjadi character baru (new) pada suatu string (word).
    temp = ""
    for character in word:
        if character != old:
            temp += character
    return temp       

def length(arr):
# fungsi menghasilkan jumlah elemen pada arr, berfungsi seperti len() pada python 3
    total = 0
    for i in arr:
        total += 1
    return total

def manualSplit(word, delimiter):
# Fungsi mengubah string menjadi elemen array yang dipisahkan oleh suatu character, berfungsi seperti fungsi split() di python 3.
    sumElement = 1
    for i in word:
        if i == delimiter:
            sumElement += 1
    li = [" " for i in range(sumElement)]
    temp = ""
    idx = 0
    j = 0
    for character in word:
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
# Sering digunakan ketika mengecek apabila input string kosong
    empty = True
    if length(word) == 0:
        return empty
    for i in word:
        if i != " ":
            empty = False
    return empty

def convertData(file):
# Fungsi ini mengonversi data pada file csv menjadi matrix
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

def getGameID(dataMatrix):
# Fungsi menghasilkan ID game terbaru, yakni pada urutan paling terakhir dalam toko game
    id = "GAME"
    element = length(dataMatrix)
    id += str("{0:03}".format(element))
    return id

def isInData(dataMatrix, element):
# Fungsi menghasilkan true apabila element terdapat di dalam matriks data
    found = False
    if element in (item for line in dataMatrix for item in line):
        found = True
    return found

def retrieveIdx(dataMatrix, element):
# Fungsi menghasilkan index matriks pertama kali elemen masukan ditemukan
# Prekondisi : elemen harus ada di matriks toko game
    i = 0
    while element not in dataMatrix[i] and i < (length(dataMatrix)-1):
        i += 1
    return i