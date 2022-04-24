# Module Mengubah Stok Game di Toko Game
# Kontributor : Enrique Alifio Ditya/16521253

import functions as func

def changeStock(dataMtx):
# Prosedur mengubah stok game pada matriks toko game
# I.S dataMtx terdefinisi, F.S elemen 'stok' pada salah satu baris dataMtx ditambahkan/dikurangi
# KAMUS LOKAL
#   id, action : string
#   idx, initial, addWith, final : integer
#   dataMtx : matrix of strings
# ALGORITMA
    print()
    id = func.inputID(dataMtx)
    print()
    idx = func.retrieveIdx(dataMtx, id, 0)
    initial = int(dataMtx[idx][5])
    addWith = int(input("Masukkan jumlah: "))
    while func.isWhitespace(addWith):
        print()
        print("Input tidak boleh kosong.")
        addWith = int(input("Masukkan jumlah: "))
        print()
    action = ""
    if addWith > 0: action = "ditambahkan." 
    else: action = "dikurangi."
    final = initial + addWith
    print()
    if final < 0:
        print("Stok game", dataMtx[idx][1], "gagal dikurangi karena stok kurang. Stok sekarang:", dataMtx[idx][5])
    else:
        dataMtx[idx][5] = str(final)
        print("Stok game", dataMtx[idx][1], "berhasil", action, "Stok sekarang:", dataMtx[idx][5])
    return
