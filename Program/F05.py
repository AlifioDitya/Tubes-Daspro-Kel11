from Program.functions import inputID
import functions as func

def changeAttr(dataMtx):
# Prosedur mengubah atribut game pada toko game berdasarkan ID
# I.S dataMtx terdefinisi, F.S elemen dataMtx termodifikasi
    id = func.inputID(dataMtx)
    name = input("Masukkan nama game: ")
    ctgry = input("Masukkan kategori: ")
    year = input("Masukkan tahun rilis: ")
    price = input("Masukkan harga: ")
    idx = func.retrieveIdx(dataMtx, id)
    arr = [name,ctgry,year,price]
    for i in range(1,5):
        if not func.isWhitespace(arr[i-1]):
            dataMtx[idx][i] = arr[i-1]
    return
