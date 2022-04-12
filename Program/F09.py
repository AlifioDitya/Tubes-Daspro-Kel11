import functions as func

def list_game(mtxGame, mtxKepemilikan, userid):
# Prosedur memberikan daftar game yang dimiliki pengguna
    count = 0
    for i in range(func.length(mtxKepemilikan)):
        if mtxKepemilikan[i][1] == userid:
            count += 1
    gameID = [" " for i in range(count)]
    j = 0
    for i in range(func.length(mtxKepemilikan)):
        if mtxKepemilikan[i][1] == userid:
            gameID[j] = mtxKepemilikan[i][0]
            j += 1

    if func.length(gameID) == 0:
        print("Maaf anda belum punya game.")
    else:
        arrGame = [["id","nama","kategori","tahun_rilis","harga"]] + [" " for game in gameID]
        i = 1
        for id in gameID:
            searchedIdx = func.retrieveIdx(mtxGame, id, 0)
            arrGame[i] = [mtxGame[searchedIdx][0],mtxGame[searchedIdx][1],mtxGame[searchedIdx][2],mtxGame[searchedIdx][3],mtxGame[searchedIdx][4]]
            i += 1
        func.drawTable(arrGame)
