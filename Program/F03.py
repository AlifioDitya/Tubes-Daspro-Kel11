# Nama Fungsi : Fungsi Login (F03)
# Fungsi untuk login pengguna saat awal program dimulai, mengembalikan informasi dari pengguna yang login.
# Kontributor : Victoria Angelique / 16521460, Enrique Alifio Ditya / 16521253

from B01 import decipher
import functions as func

def login(userMtx):
# Fungsi untuk login pengguna saat awal program dimulai, mengembalikan informasi dari pengguna yang login.

# Asumsikan data user sudah tersedia, berikut data username beserta dengan passwordnya.

#   username, password :
#   alifioditya, fio16521253
#   victoriangelique, angie16521460
#   yobeldc, yobel16521415
#   ramarezky, rama16521352
#   guest, guest123
#   guestadmin, guest123

# KAMUS LOKAL
#   username, password : string
#   name, userID, userRole : string
# ALGORITMA
    print()
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    print()
    # looping ketika log in gagal 
    while not func.isInData(userMtx, username, 1) or (func.isInData(userMtx, username, 1) and password != decipher(userMtx[func.retrieveIdx(userMtx, username, 1)][3], "Vigenere16521253")):
        print("Password atau username salah atau tidak ditemukan.")
        print()
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        print()
    name = userMtx[func.retrieveIdx(userMtx, username, 1)][2]
    func.loading("Logging in")
    try:
        print('''

 █───█ █▀▀▀ █─── █▀▀▀ █▀▀█ █▀▄▀█ █▀▀▀ 
 █▄█▄█ █▀▀▀ █─── █─── █──█ █─▀─█ █▀▀▀ 
  ▀ ▀  ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀   ▀ ▀▀▀▀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠱⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠤⠤⣄⠀⠀⠀⠀⠀⡇⢰⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠖⠂⣉⣠⠤⠤⢤⡈⢆⠀⠀⠀⢸⠁⠘⠀⠀⠀
    ⠀⠀⠀⠀⠀⣀⠤⠒⣈⣡⠤⠔⠛⠉⠁⠀⠀⠀⠀⢧⠈⡄⠀⠀⡞⣰⡆⠀⠀⠀
    ⠀⠀⠀⠰⢁⡴⠞⠋⠁⠀⠀⠀⠀⠀⢀⠴⠛⠓⠂⠘⡆⠰⡀⡜⢱⡿⠀⠀⠀⠀
    ⠀⠀⠀⢰⣼⡇⠀⠀⡠⠶⠶⠂⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⢿⣧⡿⠃⠀⠀⠀⠀
    ⠀⠀⠀⠈⣿⣿⡀⠈⠀⠀⠀⢠⣴⣶⣿⣿⡇⠀⠀⠀⠀⡇⠘⡟⠁⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢸⣿⣧⠀⠀⠀⠀⠘⢿⡟⣛⡻⣃⣠⣴⡶⠟⠀⠀⢰⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢫⢻⣆⠀⣀⣀⣠⣤⣶⡿⠿⠛⠋⠁⢰⣿⡆⠀⠀⡇⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢈⣎⠙⠛⠛⢛⣫⣽⣧⡀⠀⠀⠀⠀⠈⠛⠃⠀⠀⠸⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⡴⣹⡿⡔⣶⣿⣿⠿⠛⠋⠁⠀⠀⠀⣿⠳⡄⢀⣤⡄⠀⢧⠀⠀⠀⠀
    ⠀⠀⠀⡘⢠⡟⠀⢳⠉⢱⡏⠉⠣⠒⢲⠀⠀⠀⠯⢾⣭⣼⡿⠷⠀⠘⡀⠀⠀⠀
    ⠀⠀⠀⠁⠉⠀⠀⠀⠁⠉⠁⠀⠀⠀⠉⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠁⠀⠀⠀
    '''
    )
    except UnicodeEncodeError:
        print()
    print("Halo " + name + "! Selamat datang di Binomo.")
    print()
    input("Klik enter untuk memasuki main menu." )
    userID = userMtx[func.retrieveIdx(userMtx, username, 1)][0]
    userRole = userMtx[func.retrieveIdx(userMtx, username, 1)][4]
    return (userID, userRole)  # informasi pengguna yang sedang mengoperasikan sistem
