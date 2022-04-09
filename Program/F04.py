import functions as func

def addGame(dataMtx):
    name = input("Masukkan nama game: ")
    ctgry = input("Masukkan kategori: ")
    year = input("Masukkan tahun rilis: ")
    price = input("Masukkan harga: ")
    stock = input("Masukkan stok awal: ")
    while (name == "" or ctgry == "" or year == "" or price == "" or stock == ""):
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        name = input("Masukkan nama game: ")
        ctgry = input("Masukkan kategori: ")
        year = input("Masukkan tahun rilis: ")
        price = input("Masukkan harga: ")
        stock = input("Masukkan stok awal: ")
    id = func.getGameID(dataMtx)
    updated = dataMtx + [[id, name, ctgry, year, price, stock]]
    return updated
