# Soal No.3 
# NIM/Nama : 16521460/Victoria Angelique
# Tanggal : 15 April 2022
# Deskripsi : Membuat program untuk membaca masukkan sejumlah nilai mata kuliah dan mengembalikan
# berapa banyak siswa yang lulus dan tidak lulus serta menghitung rata-ratanya 

# Kamus 
# nilai, lulus, tdklulus, rata, jumlahInput: integer 

# Algoritma 

# mulai

# deklarasi variabel awal
nilai = int(input())
siswa = 0
rata = 0
lulus = 0 
tdklulus = 0
jumlahInput = 0

# validasi dan pengecekkan nilai 
while(nilai != -9999):
    if(nilai >= 0 and nilai <= 100):
        if(nilai < 40):
            tdklulus += 1
            rata += nilai
            siswa += 1
        elif(nilai >= 40):
            lulus += 1
            rata += nilai
            siswa += 1
        else: # di antara 50 dan 100
            rata += nilai
            siswa += 1
    nilai = int(input())
    jumlahInput += 1

# Mencetak output
if(siswa == 0 and jumlahInput == 0):
    print("Data nilai kosong")
elif(siswa == 0 and jumlahInput != 0):
    print("0")
else:
    rata = rata / siswa
    print(siswa)
    print(lulus)
    print(tdklulus)
    print("%.2f" % (rata))