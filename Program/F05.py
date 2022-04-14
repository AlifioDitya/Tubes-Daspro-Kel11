import functions as func

def changeAttr(dataMtx):
# Fungsi mengubah atribut game pada toko game berdasarkan ID
    print()
    id = func.inputID(dataMtx)
    name = input("Masukkan nama game: ")
    ctgry = input("Masukkan kategori: ")
    year = input("Masukkan tahun rilis: ")
    price = input("Masukkan harga: ")
    idx = func.retrieveIdx(dataMtx, id, 0)
    arr = [name,ctgry,year,price]
    for i in range(1,5):
        if not func.isWhitespace(arr[i-1]):
            dataMtx[idx][i] = arr[i-1]
    print()
    print("Data game " + str(dataMtx[idx][1]) + " berhasil diubah.")
    return
