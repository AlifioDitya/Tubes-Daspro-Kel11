import functions as func

def topup(dataMtx):
# Prosedur melakukan topup saldo untuk user tertentu
    username = input("Masukkan username: ")
    CekUsername = func.isInData(dataMtx,username,1)
    while not CekUsername:
        print("Username “" + username + "” tidak ditemukan.")
        username = input("Masukkan username: ")
    idx = func.retrieveIdx(dataMtx,username,1)
    tambah = int(input("Masukkan saldo: "))
    while (int(dataMtx[idx][5]) + tambah) < 0:
        print("Masukan tidak valid.")
        tambah = int(input("Masukkan saldo: "))
    dataMtx[idx][5] = str(int(dataMtx[idx][5]) + tambah)
    nama = dataMtx[idx][2]
    print("Top up berhasil. Saldo " + nama + " bertambah menjadi " + str(dataMtx[idx][5]) + ".")
    return