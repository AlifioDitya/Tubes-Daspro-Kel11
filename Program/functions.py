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

def manualSplit(word, delimiter):
# Fungsi mengubah string menjadi elemen array yang dipisahkan oleh suatu character, berfungsi seperti fungsi split() di python 3.
    sumElement = 0
    for i in word:
        if i == delimiter:
            sumElement += 1
    li = [" " for i in range(sumElement)]
    temp = ""
    idx = 0
    for character in word:
        if character != delimiter:
            temp += character
        else:
            li[idx] = temp
            temp = ""
            idx += 1
    return li

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

def convertData(file):
# Fungsi ini mengonversi data pada file csv menjadi matrix
    f = open(file, "r")
    raw = f.readlines()
    f.close()
    arr = [replaceChar(line, "\n", "") for line in raw]
    matrix = [[] for i in range(countRow(file))]
    i = 0
    for line in arr:
        matrix[i] = manualSplit(line, ";")
        i += 1
    return matrix  