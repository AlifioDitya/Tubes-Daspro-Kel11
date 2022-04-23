# File 

import functions as func

def getGameID(dataMatrix):
# Fungsi menghasilkan ID game terbaru, yakni pada urutan paling terakhir dalam toko game
    id = "GAME"
    element = func.length(dataMatrix)
    id += str("{0:03}".format(element))
    return id

def addGame(dataMtx):
# Prosedur menambahkan game pada matriks toko game
# I.S dataMtx terdefinisi, F.S ditambahkan elemen ke dataMtx
    print()
    name = input("Masukkan nama game: ")
    while func.isInData(dataMtx, name, 1):
        print()
        print("Game sudah ada di toko!")
        print()
        name = input("Masukkan nama game: ")
    ctgry = input("Masukkan kategori: ")
    year = input("Masukkan tahun rilis: ")
    price = input("Masukkan harga: ")
    stock = input("Masukkan stok awal: ")
    if (func.isWhitespace(name) or func.isWhitespace(ctgry) or func.isWhitespace(year) or func.isWhitespace(price) or func.isWhitespace(stock)):
        print()
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        return
    id = getGameID(dataMtx)
    dataMtx += [[id, name, ctgry, year, price, stock]]
    print()
    print("Selamat! Berhasil menambahkan game " + name + ".")
    return
