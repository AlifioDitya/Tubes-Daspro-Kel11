# Module Menambah Game ke Toko Game
# Kontributor : Enrique Alifio Ditya/16521253 

import functions as func

def getGameID(dataMatrix):
# Fungsi menghasilkan ID game terbaru, yakni pada urutan paling terakhir dalam toko game
# KAMUS LOKAL
#   id : string
#   element : integer
#   dataMatrix : matrix of strings
# ALGORITMA
    id = "GAME"
    element = func.length(dataMatrix)
    id += str("{0:03}".format(element))
    return id

def addGame(dataMtx):
# Prosedur menambahkan game pada matriks toko game
# I.S dataMtx terdefinisi, F.S ditambahkan elemen ke dataMtx
# KAMUS LOKAL
#   name, ctgry, year, price, stock : string
#   id : string
#   dataMtx : matrix of strings
# ALGORITMA
    print()
    name = input("Masukkan nama game: ")
    while func.isInData(dataMtx, name, 1):
        print()
        print("Game sudah ada di toko!")     # Pesan apabila game sudah ada di toko
        print()
        name = input("Masukkan nama game: ")
    ctgry = input("Masukkan kategori: ")
    year = input("Masukkan tahun rilis: ")
    price = input("Masukkan harga: ")
    stock = input("Masukkan stok awal: ")
    while (func.isWhitespace(name) or func.isWhitespace(ctgry) or func.isWhitespace(year) or func.isWhitespace(price) or func.isWhitespace(stock)):
        print()
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")     # Pesan apabila informasi masukan tidak lengkap
        print()
    id = getGameID(dataMtx)
    dataMtx += [[id, name, ctgry, year, price, stock]]
    print()
    print("Selamat! Berhasil menambahkan game " + name + ".")
    return
