# Nama Fungsi : Fungsi Save (F16)
# Fungsi save akan menyimpan perubahan data ke dalam csv sesuai dengan permintaan pengguna 
# Kontributor : Victoria Angelique / 16521460, Enrique Alifio Ditya / 16521253

import os
import functions as func
import variables as var
from config import ROOT_DIR

def mtxToCSV(mtx):
# Prosedur mengubah bentuk data dari matriks ke string terpisah oleh titik koma
# KAMUS LOKAL
#   temp : string
#   line : array of string
#   mtx : matrix of string
# ALGORITMA
    temp = ""
    for line in mtx:
        for element in line:
            if element != line[func.length(line)-1]:
                temp += str(element) + ";"
            else: temp += str(element) + "\n"
    return temp

def writeCSV(matrix, file):
# Prosedur melakukan penulisan data berbentuk matriks ke dalam file csv
# KAMUS LOKAL
#   f : SEQFILE
#   matrix : matrix
#   file : string
# ALGORITMA
    f = open(file, "w")
    f.write(mtxToCSV(matrix))
    f.close()
    return

def save():
# Prosedur melakukan penyimpanan data ke dalam file csv
# I.S perubahan data belum tersimpan 
# F.S perubahan data tersimpan dalam csv
# KAMUS LOKAL
#   folder : string
# Asumsi folder yang dicari berada di bawah level folder 'Tubes-Daspro-Kel11'
    folder = input("Masukkan nama folder penyimpanan: ")
    while func.isWhitespace(folder):
        print()
        print("Mohon input nama folder penyimpanan data.")
        print()
        folder = input("Masukkan nama folder penyimpanan: ")
    path = os.path.join(ROOT_DIR, folder)
    if os.path.exists(path):
        filedir = os.path.join(path, "user.csv")
        writeCSV(var.user, filedir)
        filedir = os.path.join(path, "game.csv")
        writeCSV(var.game, filedir)
        filedir = os.path.join(path, "riwayat.csv")
        writeCSV(var.riwayat, filedir)
        filedir = os.path.join(path, "kepemilikan.csv")
        writeCSV(var.kepemilikan, filedir)
    else:
        os.mkdir(path)
        filedir = os.path.join(path, "user.csv")
        writeCSV(var.user, filedir)
        filedir = os.path.join(path, "game.csv")
        writeCSV(var.game, filedir)
        filedir = os.path.join(path, "riwayat.csv")
        writeCSV(var.riwayat, filedir)
        filedir = os.path.join(path, "kepemilikan.csv")
        writeCSV(var.kepemilikan, filedir)
    print()
    func.loading("Saving")
    print()
    print("Data telah tersimpan pada folder " + folder)
    return