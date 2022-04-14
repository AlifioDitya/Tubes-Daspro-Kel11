import functions as func

def help(userType):
# Prosedur untuk menampilkan panduan penggunaan sistem
    if userType.lower() == "admin":
        print("============ HELP ============\n1. register - Untuk melakukan registrasi user baru\n2. login - Untuk melakukan login ke dalam sistem\n3. tambah_game - Untuk menambah game yang dijual pada toko\n4. list_game_toko - Untuk melihat list game yang dijual pada toko\n5. search_game_at_store - Untuk mencari sebuah game yang dijual pada toko\n6. topup - Untuk menambahkan saldo dari user\n")
    else:
        print("============ HELP ============\n1. login - Untuk melakukan login ke dalam sistem\n2. list_game_toko - Untuk melihat list game yang dijual pada toko\n3. buy_game - Untuk membeli game yang terdapat pada toko\n4. list_game - Untuk melihat game yang dimiliki User\n5. search_my_game - Untuk mencari salah satu game yang dimiliki User\n6. search_game_at_store - Untuk mencari sebuah game yang dijual pada toko\n7. riwayat - Untuk melihat riwayat pembelian User")
