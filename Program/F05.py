# Module Mengubah Game pada Toko Game
# Kontributor : Enrique Alifio Ditya/16521253

import functions as func

def changeAttr(dataMtx):
# Prosedur mengubah atribut game pada toko game berdasarkan ID
# I.S dataMtx terdefinisi, F.S elemen dataMtx sebagian tergantikan
# KAMUS LOKAL
#   id, name, ctgry, year, price : string
#   idx, i : integer
#   arr : array of strings
#   dataMtx : matrix of strings
# ALGORITMA
    print()
    id = func.inputID(dataMtx)
    name = input("Masukkan nama game: ")
    ctgry = input("Masukkan kategori: ")
    year = input("Masukkan tahun rilis: ")
    price = input("Masukkan harga: ")
    idx = func.retrieveIdx(dataMtx, id, 0)   # Mencari indeks matriks dari game yang dispesifikasikan
    arr = [name,ctgry,year,price]
    for i in range(1,5):
        if not func.isWhitespace(arr[i-1]):
            dataMtx[idx][i] = arr[i-1]
    print()
    print("Data game " + str(dataMtx[idx][1]) + " berhasil diubah.")
    return
