import functions as func
from B01 import decipher

def login(userMtx):
# Fungsi untuk login pengguna saat awal program dimulai, mengembalikan informasi dari pengguna yang login.
# KAMUS LOKAL
#   username, password : string
#   name, userID, userRole : string
# ALGORITMA
    print()
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    # looping ketika log in gagal 
    while not func.isInData(userMtx, username, 1) or (func.isInData(userMtx, username, 1) and password != password != decipher(userMtx[func.retrieveIdx(userMtx, username, 1)][3], "Vigenere16521253")):
        print("Password atau username salah atau tidak ditemukan.")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
    name = userMtx[func.retrieveIdx(userMtx, username, 1)][2]
    print()
    print("Halo " + name + "! Selamat datang di Binomo.")
    userID = userMtx[func.retrieveIdx(userMtx, username, 1)][0]
    userRole = userMtx[func.retrieveIdx(userMtx, username, 1)][4]
    return (userID, userRole)  # informasi pengguna yang sedang mengoperasikan sistem