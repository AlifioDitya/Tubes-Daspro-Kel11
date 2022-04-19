import functions as func
from B01 import cipher

def UserID (user):
# Fungsi membuat / generate user ID secara otomatis dengan kode unik 
# KAMUS LOKAL
#   id : string
#   element : integer
# ALGORITMA
    id = "USER"
    element = func.length(user)
# mencetak user ke- tergantung jumlah data user yang terdaftar dalam csv user
    if (element < 10):
        id += str("00{}".format(element))
    elif(element < 100):
        id += str("0{}".format(element))
    else: 
        id += str("{}".format(element))
    return id

def register(userMtx):
# Prosedur register melakukan registrasi pengguna bertipe user
# I.S. data userMtx sudah terdefinisi secara manual oleh sistem 
# F.S. data userMtx diperbeharui dengan data yang baru
# KAMUS LOKAL
    # name, username : string 
    # password, id : string 
    # validasiUsername : arr[0..11] of characters
    # valid : boolean
    # i : integer
# ALGORITMA
    print()
    name = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    # Validasi username per character 
    validasiUsername = ["-","_","0","1","2","3","4","5","6","7","8","9"]
    # Asumsikan username sudah valid
    valid = True
    errMessage = ""
    # Looping kevalidan character username 
    for i in range(func.length(username)):
        if not (func.isInArr(username[i],validasiUsername) or (ord(username[i]) >= 97 and ord(username[i]) <= 122) or (ord(username[i]) >= 65 and ord(username[i]) <= 90)): 
            valid = False
            errMessage = "Username tidak valid."
            break
    
    # Cek apabila username sudah ada di data user
    for i in range(func.length(userMtx)):
        if username == userMtx[i][1]:
            valid = False
            errMessage = "Username " + str(username) + " sudah terpakai, silakan menggunakan username lain."
            break

    password = input("Masukkan password: ")
    print()
    if valid:
        id = UserID(userMtx)
        # menyimpan data user dalam matrix
        dataUsers = [id,username,name,cipher(password),"user","0"]
        userMtx += [dataUsers]
        print("Username " + username + " telah berhasil register ke dalam Binomo.")
    else:
        print(errMessage)
    return