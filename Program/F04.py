import functions as func

def addGame(dataMtx):
# Prosedur menambahkan game pada matriks toko game
# I.S dataMtx terdefinisi, F.S ditambahkan elemen ke dataMtx
    name = input("Masukkan nama game: ")
    ctgry = input("Masukkan kategori: ")
    year = input("Masukkan tahun rilis: ")
    price = input("Masukkan harga: ")
    stock = input("Masukkan stok awal: ")
    while (func.isWhitespace(name) or func.isWhitespace(ctgry) or func.isWhitespace(year) or func.isWhitespace(price) or func.isWhitespace(stock)):
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        name = input("Masukkan nama game: ")
        ctgry = input("Masukkan kategori: ")
        year = input("Masukkan tahun rilis: ")
        price = input("Masukkan harga: ")
        stock = input("Masukkan stok awal: ")
    id = func.getGameID(dataMtx)
    dataMtx += [[id, name, ctgry, year, price, stock]]
    print("Selamat! Berhasil menambahkan game " + name + ".")
    return
