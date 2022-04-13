import functions as func

def topup(mtxUserData):
# Prosedur melakukan topup saldo untuk user tertentu
    username = input("Masukkan username: ")
    while not func.isInData(mtxUserData, username, 1):
        print("Username \"" + str(username) + "\" tidak ditemukan." )
        username = input("Masukkan username: ")
    idx = func.retrieveIdx(mtxUserData, username, 1)
    addSaldo = int(input("Masukkan saldo: "))
    while (addSaldo + int(mtxUserData[idx][5])) < 0:
        print("Masukan tidak valid.")
        addSaldo = int(input("Masukkan saldo: "))
    mtxUserData[idx][5] = str(addSaldo + int(mtxUserData[idx][5]))
    return
