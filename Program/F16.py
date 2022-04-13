import functions as func

def mtxToCSV(mtx):
# Prosedur mengubah bentuk data dari matriks ke string terpisah oleh titik koma
    temp = ""
    for line in mtx:
        for element in line:
            if element != line[func.length(line)-1]:
                temp += str(element) + ";"
            else: temp += str(element) + "\n"
    return temp

def save(matrix, file):
# Prosedur melakukan penulisan data berbentuk matriks ke dalam file csv tujuan
    f = open(file, "w")
    f.write(mtxToCSV(matrix))
    f.close()
    return