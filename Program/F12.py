# Module Topup
# Kontributor : Rama Maulana Rezky/16521325, Enrique Alifio Ditya/16521253

import functions as func

def topup(dataMtx):
# Prosedur melakukan topup saldo untuk user tertentu
# KAMUS LOKAL
#   username, name : string
#   CekUsername : boolean
#   idx, tambah : integer
#   dataMtx : matrix of string
# ALGORITMA
    print()
    username = input("Masukkan username: ")
    CekUsername = func.isInData(dataMtx,username,1)
    if not CekUsername and func.isWhitespace(username):
        print()
        print("Username “" + username + "” tidak ditemukan.")
        return
    idx = func.retrieveIdx(dataMtx,username,1)
    tambah = int(input("Masukkan saldo: "))
    while (int(dataMtx[idx][5]) + tambah) < 0:
        print("Masukan tidak valid.")
        tambah = int(input("Masukkan saldo: "))
    dataMtx[idx][5] = str(int(dataMtx[idx][5]) + tambah)
    nama = dataMtx[idx][2]
    print()
    if tambah > 0:
        print("Top up berhasil. Saldo " + nama + " bertambah menjadi " + str(dataMtx[idx][5]) + ".")
    elif tambah == 0:
        print("Saldo " + nama + " tetap " + str(dataMtx[idx][5]) + ".")
    else:
        print("Penarikan saldo berhasil. Saldo " + nama + " berkurang menjadi " + str(dataMtx[idx][5]) + ".")
    return