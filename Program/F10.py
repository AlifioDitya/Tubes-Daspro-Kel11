import functions as func

def search_my_game(toko, kepemilikan, userID):
# Prosedur untuk mencari game yang dimiliki berdasarkan ID/tahun rilis
    print()
    punya_game = func.hasGame(toko, kepemilikan, userID)

    gameID = input('Masukkan ID Game: ').upper()
    tahun_rilis = str(input('Masukkan Tahun Rilis Game: '))

    searchBy = [gameID, " ", " ", tahun_rilis, " "]
    flag = [True for i in range(func.length(punya_game))]

    for i in range(func.length(searchBy)):
        if not func.isWhitespace(searchBy[i]):
            for j in range(func.length(flag)):
                if searchBy[i].lower() != str(punya_game[j][i]).lower():
                    flag[j] = False
    
    total = 0
    for i in flag:
        if i == True:
            total += 1
    
    sesuai_kriteria = [["ID", "Nama", "Kategori", "Tahun Rilis", "Harga"]] + [[" " for j in range(6)] for i in range(total)]

    j = 1
    for i in range(func.length(flag)):
        if flag[i]:
            sesuai_kriteria[j] = punya_game[i]
            j += 1

    if func.length(sesuai_kriteria) == 1:
        print()
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria.")
        return
    else:
        stopShow = False
        while not stopShow:
            print()
            print("Daftar game: ")
            func.drawTable(sesuai_kriteria)
            print()
            input("Klik Enter untuk kembali ke main menu." )
            stopShow = True
        return