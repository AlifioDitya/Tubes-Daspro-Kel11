import functions as func

def changeAttr(dataMtx):
# Fungsi mengubah atribut game pada toko game berdasarkan ID
    id = input("Masukkan ID game: ")
    while not func.isInData(dataMtx, id) or func.isWhitespace(id):
        if func.isWhitespace(id):
            print("ID game tidak boleh kosong.")
        elif not func.isInData(dataMtx, id):
            print("ID game tidak ada.")
        id = input("Masukkan ID game: ")
    name = input("Masukkan nama game: ")
    ctgry = input("Masukkan kategori: ")
    year = input("Masukkan tahun rilis: ")
    price = input("Masukkan harga: ")
    idx = func.retrieveIdx(dataMtx, id)
    arr = [name,ctgry,year,price]
    for i in range(1,5):
        if not func.isWhitespace(arr[i-1]):
            dataMtx[idx][i] = arr[i-1]
    return dataMtx
