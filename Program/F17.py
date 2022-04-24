# Nama Fungsi: Fungsi Exit (F17)
# Deskripsi : Fungsi melakukan terminasi looping main program dengan mengembalikan False jika user ingin keluar sistem. 
# Fungsi exit ini juga akan memanggil prosedur save apabila user ingin menyimpan perubahan terlebih dahulu
# Kontributor : Victoria Angelique / 16521460, Enrique Alifio Ditya / 16521253

from F16 import save

def keluar():
# Fungsi melakukan terminasi looping main program dengan mengembalikan False jika user ingin keluar sistem.
# Prosedur save dilakukan apabila user ingin menyimpan perubahan terlebih dahulu.
# I.S Program masih berjalan 
# F.S Program berhenti 
# KAMUS LOKAL 
#   running : boolean 
#   keluar : string
# ALGORITMA
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
