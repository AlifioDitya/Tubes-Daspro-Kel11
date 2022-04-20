import functions as func

def drawSortedMtx(dataMtx):
# Prosedur menggambar matriks data yang sudah terurut
# I.S dataMtx terdefinisi, F.S dataMtx terurut dan tergambar
    print()
    stopShow = False
    while not stopShow:
        sortBy = input("Skema sorting: ")
        while not func.isWhitespace(sortBy) and sortBy.lower() != "tahun-" and sortBy.lower() != "tahun+" and sortBy.lower() != "harga-" and sortBy.lower() != "harga+":
            print()
            print("Skema sorting tidak valid!")
            print()
            sortBy = input("Skema sorting: ")
        print()
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
        print()
        print("Klik Enter untuk kembali ke main menu.")
        input()
        stopShow = True
    return