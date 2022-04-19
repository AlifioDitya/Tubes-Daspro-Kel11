import functions as func

def list_game(toko, kepemilikan, userID):
# Prosedur untuk menampilkan game yang dimiliki user yang sedang mengoperasikan sistem
    punya_game = [["id","nama","kategori","tahun_rilis","harga"]] + func.hasGame(toko, kepemilikan, userID)
    stopShow = False
    print()
    if func.length(punya_game) > 1:
        while not stopShow:
            print("Daftar game: ")
            func.drawTable(punya_game)
            print()
            print("Klik Enter untuk kembali ke main menu.")
            input()
            stopShow = True        
    else:
        return print('Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.')
    return
