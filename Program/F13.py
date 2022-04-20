import functions as func

def history(mtxRiwayat, userid):
# Prosedur memberikan riwayat pembelian game yang dimiliki pengguna
    count = 0
    for i in range(func.length(mtxRiwayat)):
        if mtxRiwayat[i][0] == userid:
            count += 1
    game = [" " for i in range(count)]
    j = 0
    for i in range(func.length(mtxRiwayat)):
        if mtxRiwayat[i][0] == userid:
            game[j] = mtxRiwayat[i][1]
            j += 1

    if func.length(game) == 0:
        print("Maaf, kamu tidak ada riwayat pembelian. Ketik perintah beli_game untuk beli.")
    else:
        arrGame = [["game id","nama","harga","tahun_beli"]] + [" " for i in game]
        i = 1
        for id in game:
            searchedIdx = func.retrieveIdx(mtxRiwayat, id, 1)
            arrGame[i] = [mtxRiwayat[searchedIdx][1],mtxRiwayat[searchedIdx][2],mtxRiwayat[searchedIdx][3],mtxRiwayat[searchedIdx][4]]
            i += 1
        stopShow = False
        while not stopShow:
            print()
            print("Daftar riwayat: ")
            func.drawTable(arrGame)
            print()
            input("Klik Enter untuk kembali ke main menu.")
            stopShow = True
    return
