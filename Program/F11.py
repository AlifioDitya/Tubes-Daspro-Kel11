import functions as func

def search_game_at_store(gameData):
# Prosedur mencari game pada toko game berdasarkan filter tertentu
# Asumsi input filter persis sama dengan yang tercatat pada data
    print()
    gameID = input("Masukkan ID Game: ")
    name = input("Masukkan Nama Game: ")
    price = input("Masukkan Harga Game: ")
    ctgry = input("Masukkan Kategori Game: ")
    year = input("Masukkan Tahun Rilis Game: ")

    searchBy = [gameID, name, ctgry, year, price]
    flag = [False] + [True for i in range(1, func.length(gameData))]

    for i in range(func.length(searchBy)):
        if not func.isWhitespace(searchBy[i]):
            for j in range(1, func.length(flag)):
                if searchBy[i].lower() != str(gameData[j][i]).lower():
                    flag[j] = False

    total = 0
    for i in flag:
        if i == True:
            total += 1
    
    memenuhi = [["ID", "Nama", "Kategori", "Tahun Rilis", "Harga", "Stok"]] + [[" " for j in range(6)] for i in range(total)]

    j = 1
    for i in range(func.length(flag)):
        if flag[i]:
            memenuhi[j] = gameData[i]
            j += 1

    if func.length(memenuhi) == 1:
        print()
        print("Tidak ada game pada toko yang memenuhi kriteria.")
        return
    else:
        stopShow = False
        while not stopShow:
            func.drawTable(memenuhi)
            print()
            input("Klik Enter untuk kembali ke main menu." )
            stopShow = True
        return