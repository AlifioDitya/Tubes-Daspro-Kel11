import functions as func

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
    name = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    # Validasi username per character 
    validasiUsername = ["-","_","0","1","2","3","4","5","6","7","8","9"]
    # Asumsikan username sudah valid
    valid = True 
    # Looping kevalidan character username 
    for i in range(func.length(username)):
        if(username[i] in (validasiUsername) or (ord(username[i]) >= 97 and ord(username[i]) <= 122) or (ord(username[i]) >= 65 and ord(username[i]) <= 90)): 
            pass
        else:
            valid = False
            break
    # Cek apabila username sudah ada di data user
    for line in userMtx:
        if username in line:
            valid = False
        break

    if (valid):
        password = input("Masukkan password: ")
        id = UserID(userMtx)
        # menyimpan data user dalam matrix
        dataUsers = [id,username,name,password,"user",str(0)]
        userMtx += [dataUsers]
        print("Username " + username + " telah berhasil register ke dalam Binomo.")
    else:
        print("Username tidak valid")
    return