# Module Daftar Game yang Dimiliki
# Kontributor : Yobel Dean Christopher/16521415, Enrique Alifio Ditya/16521253

import functions as func

def list_game(toko, kepemilikan, userID):
# Prosedur untuk menampilkan game yang dimiliki user yang sedang mengoperasikan sistem
# KAMUS LOKAL
#   punya_game : matrix of strings
#   stopShow : boolean
# ALGORITMA
    punya_game = [["id","nama","kategori","tahun_rilis","harga"]] + func.hasGame(toko, kepemilikan, userID)
    stopShow = False
    print()
    if func.length(punya_game) > 1:
        while not stopShow:
            print("Daftar game yang dimiliki: ")
            func.drawTable(punya_game)
            print()
            input("Klik Enter untuk kembali ke main menu.")
            stopShow = True        
    else:
        return print('Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.')
    return
