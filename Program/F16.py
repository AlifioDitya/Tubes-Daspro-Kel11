import os
import functions as func
import variables as var
from config import ROOT_DIR
from time import sleep

def mtxToCSV(mtx):
# Prosedur mengubah bentuk data dari matriks ke string terpisah oleh titik koma
    temp = ""
    for line in mtx:
        for element in line:
            if element != line[func.length(line)-1]:
                temp += str(element) + ";"
            else: temp += str(element) + "\n"
    return temp

def writeCSV(matrix, file):
# Prosedur melakukan penulisan data berbentuk matriks ke dalam file csv
    f = open(file, "w")
    f.write(mtxToCSV(matrix))
    f.close()
    return

def saving():
    print("Saving", end="\r")
    sleep(0.25)
    print("Saving.",end="\r")
    sleep(0.25)
    print("Saving..",end="\r")
    sleep(0.25)
    print("Saving...",end="\r")
    sleep(0.25)
    print()

def save():
# Prosedur melakukan penyimpanan data ke dalam file csv
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
    saving()
    print("Data telah tersimpan pada folder " + folder)
    return