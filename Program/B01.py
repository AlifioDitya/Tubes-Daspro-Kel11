import functions as func

def findKeystream (plaintext, key):
# Fungsi mengenerate keystream untuk dipakai pada proses ciphering/deciphering pesan
    keystream = ""
    if func.length(plaintext) < func.length(key):
        for i in range(func.length(plaintext)):
            keystream += key[i]
    else:
        keystream += key
        keystream += findKeystream (plaintext[func.length(keystream):], key)
    return keystream

def cipher(plaintext):
# Fungsi mengembalikan pesan tersembunyi dengan algoritma keyed vigenere cipher
# Diasumsikan string masukan tidak akan memiliki karakter selain yang terdapat pada variabel characters di subprogram ini
    characters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!@#$%^&*()-_=+:/"
    key = "Vigenere16521253"
    keystream = findKeystream(plaintext, key)
    shiftedC = ""
    ciphertext = ""
    for i in range(func.length(plaintext)):
        for j in range(func.length(characters)):
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
# Fungsi melakukan deciphering pesan tersembunyi oleh algoritma keyed vigenere
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
