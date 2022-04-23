# Module Bonus Magic Conch Shell
# Kontributor : Enrique Alifio Ditya/16521253

from datetime import datetime as dt

def lcg():
# Fungsi menghasilkan angka dalam range [0..6] secara pseudorandom 
# dengan nilai 'seed' diambil dari milisecond waktu sekarang
# Nilai a dan b pada algoritma lcg ini mengikuti yang digunakan oleh Microsoft Visual C++
# KAMUS LOKAL
#   x, a, b : integer
# ALGORITMA
    x = int(dt.now().strftime("%f"))
    a = 214013
    b = 2531011
    return ((a*x + b)%7)

def mcs():
# Prosedur magic conch shell memberikan jawaban secara pseudorandom dengan memanfaatkan prosedur lcg
# I.S program utama berjalan, F.S fitur mcs dijalankan.
# KAMUS LOKAL
#   n : integer
# ALGORITMA
    print()
    input("Apa pertanyaanmu? ")
    n = lcg()
    if n == 0:
        print("Iya.")
    elif n == 1:
        print("Tidak.")
    elif n == 2:
        print("Mungkin.")
    elif n == 3:
        print("Bisa jadi.")
    elif n == 4:
        print("Tergantung.")
    elif n == 5:
        print("Belum tentu.")
    elif n == 6:
        print("Ya ndak tau kok tanya saya.")