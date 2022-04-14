import functions as func

def drawSortedMtx(dataMtx):
# Prosedur menggambar matriks data yang sudah terurut
# I.S dataMtx terdefinisi, F.S dataMtx terurut dan tergambar
    sortBy = input("Skema sorting: ")
    while not func.isWhitespace(sortBy) and sortBy.lower() != "tahun-" and sortBy.lower() != "tahun+" and sortBy.lower() != "harga-" and sortBy.lower() != "harga+":
        print("Skema sorting tidak valid!")
        sortBy = input("Skema sorting: ")
    print("Daftar game: ")
    if func.isWhitespace(sortBy):
        func.drawTable(dataMtx)
    elif sortBy.lower() == "tahun+":
        func.drawTable(func.sortMtxCol(dataMtx, 3, 0))
    elif sortBy.lower() == "tahun-":
        func.drawTable(func.sortMtxCol(dataMtx, 3, 1))
    elif sortBy.lower() == "harga+":
        func.drawTable(func.sortMtxCol(dataMtx, 4, 0))
    elif sortBy.lower() == "harga-":
        func.drawTable(func.sortMtxCol(dataMtx, 4, 1))