import functions as func

def addGame(dataMtx):
    name = input("Masukkan nama game: ")
    ctgry = input("Masukkan kategori: ")
    year = input("Masukkan tahun rilis: ")
    price = input("Masukkan harga: ")
    stock = input("Masukkan stok awal: ")
    while (func.isWhitespace(name) or func.isWhitespace(ctgry) or func.isWhitespace(year) or func.isWhitespace(price) or func.isWhitespace(stock)):
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        name = input("Masukkan nama game: ")
        ctgry = input("Masukkan kategori: ")
        year = int(input("Masukkan tahun rilis: "))
        price = int(input("Masukkan harga: "))
        stock = int(input("Masukkan stok awal: "))
    id = func.getGameID(dataMtx)
    updated = dataMtx + [[id, name, ctgry, year, price, stock]]
    return updated
