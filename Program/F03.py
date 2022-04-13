import functions as func

def login(userMtx):
# Fungsi untuk login pengguna saat awal program dimulai, mengembalikan informasi dari pengguna yang login.
# KAMUS LOKAL
#   username, password : string
#   name, userID, userRole : string
# ALGORITMA
    print("Selamat datang di Binomo! ヽ(o^ ^o)ﾉ")
    print("Mohon login terlebih dahulu!")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    # looping ketika log in gagal, yakni ketika username tidak ada di data atau password salah
    while not func.isInData(userMtx, username, 1) or (func.isInData(userMtx, username, 1) and password != userMtx[func.retrieveIdx(userMtx, username, 1)][3]):
        print("Password atau username salah atau tidak ditemukan.")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
    name = userMtx[func.retrieveIdx(userMtx, username, 1)][2]
    print("Halo " + name + "! Selamat datang di Binomo.")
    userID = userMtx[func.retrieveIdx(userMtx, username, 1)][0]
    userRole = userMtx[func.retrieveIdx(userMtx, username, 1)][4]
    return (userID, userRole)  # informasi pengguna yang sedang mengoperasikan sistem