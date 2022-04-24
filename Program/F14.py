# Module Topup
# Kontributor : Rama Maulana Rezky/16521325, Enrique Alifio Ditya/16521253

def help(userType):
# Prosedur untuk menampilkan panduan penggunaan sistem
# I.S program berjalan, F.S tampak panduan pengoperasian sistem
# KAMUS LOKAL
#   stopShow : boolean
# ALGORITMA
    print()
    stopShow = False
    while not stopShow:
        if userType.lower() == "admin":
            print("================================ HELP ===================================")
            print("1. login - Masuk pada akun untuk mengoperasikan sistem.")
            print("2. register - Registrasi user baru.")
            print("3. tambah_game - Menambah game yang dijual pada toko.")
            print("4. ubah_game - Mengubah data game yang dijual pada toko.")
            print("5. ubah_stok - Mengubah stok game yang dijual pada toko.")
            print("6. list_game_toko - Melihat daftar game yang dijual pada toko.")
            print("7. search_game_at_store - Mencari game yang dijual pada toko.")
            print("8. topup - Menambahkan saldo dari user.")
            print("9. save - Menyimpan data pada folder yang telah dispesifikasi.")            
            print("10. logout - Logout dari akun yang digunakan.")
            print("11. exit - Stop program.")
        elif userType.lower() == "user":
            print("================================ HELP ===================================")
            print("1. login - Masuk pada akun untuk mengoperasikan sistem.")
            print("2. list_game_toko - Melihat daftar game yang dijual pada toko")
            print("3. buy_game - Membeli game dari toko.")
            print("4. list_game - Melihat game yang dimiliki.")
            print("5. search_my_game - Mencari game yang dimiliki")
            print("6. search_game_at_store - Mencari game yang dijual pada toko")
            print("7. riwayat - Daftar riwayat pembelian game.")
            print("8. extras - Fitur bonus BNMO.")
            print("9. save - Menyimpan data pada folder yang telah dispesifikasi")
            print("10. logout - Logout dari akun yang digunakan.")
            print("11. exit - Stop program.")
        else:
            print("================================ HELP ===================================")
            print()
            print("---------------------------- Fitur Admin --------------------------------")
            print("1. login - Masuk pada akun untuk mengoperasikan sistem.")
            print("2. register - Registrasi user baru.")
            print("3. tambah_game - Menambah game yang dijual pada toko.")
            print("4. ubah_game - Mengubah data game yang dijual pada toko.")
            print("5. ubah_stok - Mengubah stok game yang dijual pada toko.")
            print("6. list_game_toko - Melihat daftar game yang dijual pada toko.")
            print("7. search_game_at_store - Mencari game yang dijual pada toko.")
            print("8. topup - Menambahkan saldo dari user.")
            print("9. save - Menyimpan data pada folder yang telah dispesifikasi.")            
            print("10. logout - Logout dari akun yang digunakan.")
            print("11. exit - Stop program.")
            print()
            print("---------------------------- Fitur User ---------------------------------")
            print("1. login - Masuk pada akun untuk mengoperasikan sistem.")
            print("2. list_game_toko - Melihat daftar game yang dijual pada toko")
            print("3. buy_game - Membeli game dari toko.")
            print("4. list_game - Melihat game yang dimiliki.")
            print("5. search_my_game - Mencari game yang dimiliki")
            print("6. search_game_at_store - Mencari game yang dijual pada toko")
            print("7. riwayat - Daftar riwayat pembelian game.")
            print("8. extras - Fitur bonus BNMO.")
            print("9. save - Menyimpan data pada folder yang telah dispesifikasi")
            print("10. logout - Logout dari akun yang digunakan.")
            print("11. exit - Stop program.")
        print()
        input("Klik Enter untuk balik ke main menu.")
        stopShow = True