from F16 import save

def keluar():
# Fungsi melakukan terminasi looping main program dengan mengembalikan False jika user ingin keluar sistem.
# Prosedur save dilakukan apabila user ingin menyimpan perubahan terlebih dahulu.
    running = True
    keluar = input("Apakah anda ingin menyimpan file yang sudah diubah dalam program Binomo? (y/t): ") 
    # validasi jawaban Ya atau Tidak
    if keluar == 'Y' or keluar == 'y':
        print()
    # menyimpan data dan menutup program
        save()
        print("Terima kasih sudah menggunakan Binomo ^-^")
        running = False
    elif keluar == 'T' or keluar == 't':
        print()
        print("Terima kasih sudah menggunakan Binomo ^-^")
        running = False
    else: # input di luar Ya dan Tidak (Y/T)
        print()
        print("Input tidak valid.")
    return running
