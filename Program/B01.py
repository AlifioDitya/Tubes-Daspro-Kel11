# Module Bonus Cipher
# Kontributor : Enrique Alifio Ditya / 16521253, Nayyara Airlangga / 2106652070

import functions as func

def findKeystream (plaintext, key):
# Fungsi menghasilkan keystream untuk dipakai pada proses ciphering/deciphering pesan
# Menerima masukan suatu plaintext dan keyword, kemudian menghasilkan perulangan keyword sampai sepanjang plaintext
# Ex. input : { plaintext "helloworld", key "hola" } ; output : "holaholaho"
# KAMUS LOKAL
#   keystream, plaintext, key, temp : string
#   i : integer
# ALGORITMA
    keystream = ""
    if func.length(plaintext) < func.length(key):
        for i in range(func.length(plaintext)):
            keystream += key[i]
    else:
        keystream += key
        temp = ""
        for i in range(func.length(keystream), func.length(plaintext)):
            temp += plaintext[i]
        keystream += findKeystream (temp, key)   # rekursi apabila plaintext lebih panjang daripada key
    return keystream

def cipher(plaintext):
# Fungsi mengembalikan pesan tersembunyi dengan algoritma keyed vigenere cipher.
# Diasumsikan string masukan tidak akan memiliki karakter selain yang terdapat pada variabel characters di subprogram ini.
# Algoritma keyed vigenere cipher merupakan cipher berjenis poly alphabetic substitution. 
# Array of characters ditabulasikan kemudian plaintext dan keystream masing-masing akan menentukan kolum serta baris pemetaan dalam tabel karakter tersebut.
# Lebih jelasnya dapat dilihat di link berikut: https://youtu.be/SkJcmCaHqS0
# Credit to Udacity on YouTube.
# KAMUS LOKAL
#   characters, key, keystream, shiftedC, plaintext, ciphertext : string
#   i, j, k, x, y, idx : integer
# ALGORITMA
    characters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!@#$%^&*()-_=+:/"
    key = "Vigenere16521253"
    keystream = findKeystream(plaintext, key)
    shiftedC = ""
    ciphertext = ""
    for i in range(func.length(plaintext)):
        for j in range(func.length(characters)):
            # Menentukan baris character untuk pemetaan
            if characters[j] == plaintext[i]:
                shiftedC = ""
                for x in range(j, func.length(characters)):
                    shiftedC += characters[x]
                for y in range(j):
                    shiftedC += characters[y]
                break
        idx = 0
        for k in range(func.length(characters)):
            if characters[k] == keystream[i]:
                idx = k
                break
        ciphertext += shiftedC[idx]
    return ciphertext

def decipher (ciphertext, key):
# Fungsi melakukan deciphering pesan tersembunyi oleh algoritma keyed vigenere.
# Merupakan hasil reverse-engineering dari subprogram cipher.
# KAMUS LOKAL
#   characters, key, keystream, shiftedR, plaintext, ciphertext : string
#   i, j, k, x, y, idx : integer
# ALGORITMA
    characters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!@#$%^&*()-_=+:/"
    keystream = findKeystream(ciphertext, key)
    shiftedR = ""
    plaintext = ""
    for i in range(func.length(keystream)):
        for j in range(func.length(characters)):
            if characters[j] == keystream[i]:
                shiftedR = ""
                for x in range(j, func.length(characters)):
                    shiftedR += characters[x]
                for y in range(j):
                    shiftedR += characters[y]
                break
        idx = 0
        for k in range(func.length(shiftedR)):
            if ciphertext[i] == shiftedR[k]:
                idx = k
                break
        plaintext += characters[idx]
    return plaintext
