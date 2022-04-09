import functions as func

def changeStock(dataMtx):
# Prosedur mengubah stok game pada matriks toko game
# I.S dataMtx terdefinisi, F.S elemen 'stok' pada salah satu baris dataMtx ditambahkan/dikurangi 
    id = func.inputID(dataMtx)
    idx = func.retrieveIdx(dataMtx, id, 0)
    initial = int(dataMtx[idx][5])
    addWith = int(input("Masukkan jumlah: "))
    action = ""
    if addWith > 0: action = "ditambahkan." 
    else: action = "dikurangi."
    final = initial + addWith
    if final < 0:
        print("Stok game", dataMtx[idx][1], "gagal dikurangi karena stok kurang. Stok sekarang:", dataMtx[idx][5])
    else:
        dataMtx[idx][5] = str(final)
        print("Stok game", dataMtx[idx][1], "berhasil", action, "Stok sekarang:", dataMtx[idx][5])
    return
