import functions as func
from datetime import datetime as dt

def buy_game(toko, kepemilikan, userMtx, riwayat, userID): 
# Prosedur untuk membeli game pada toko
# I.S. toko, kepemilikan, userMtx, riwayat, dan userID terdefinisi
# F.S. Stok game ditambahkan pada data kepemilikan

# KAMUS LOKAL
#   userID, gameID : string
#   idxUser, idxGame, saldo_punya, saldo_perlu, stokGame : integer
#   toko, kepemilikan, userMtx, riwayat, gameDimiliki : matrix of strings

# ALGORITMA
    print()
    gameID = func.inputID(toko)

    idxUser = func.retrieveIdx(userMtx, userID, 0)
    idxGame = func.retrieveIdx(toko, gameID, 0)
    
    gameDimiliki = func.hasGame(toko, kepemilikan, userID)

    saldo_punya = int(userMtx[idxUser][5])
    saldo_perlu = int(toko[idxGame][4])      # Harga game
    stokGame = int(toko[idxGame][5])

    print()
    if func.isInData(gameDimiliki, toko[idxGame][0], 0):
        print("Anda sudah memiliki Game tersebut!")
        return
    elif stokGame == 0:
        print("Stok Game tersebut sedang habis!")
        return
    elif saldo_perlu > saldo_punya:
        print("Saldo anda tidak cukup untuk membeli Game tersebut!")
    else:
        toko[idxGame][5] = str(stokGame-1)   # Stok game dikurangi 1 pada toko
        userMtx[idxUser][5] = str(saldo_punya - saldo_perlu)   # Saldo user dikurangi
        kepemilikan += [[gameID, userID]]   # tambah data kepemilikan
        riwayat += [[userID, gameID, toko[idxGame][1], toko[idxGame][4], str(dt.now().strftime("%Y"))]]   # Catat di riwayat
        print(f"Game {toko[idxGame][1]} berhasil dibeli.")
        return
