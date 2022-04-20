from os import system
import functions as func
import variables as var
from F02 import register
from F03 import login
from F04 import addGame
from F05 import changeAttr
from F06 import changeStock
from F07 import drawSortedMtx
from F08 import buy_game
from F09 import list_game
from F10 import search_my_game
from F11 import search_game_at_store
from F12 import topup
from F13 import history
from F14 import help
from F15 import load
from F16 import save
from F17 import keluar
from B02 import mcs
from B03 import tictactoe

if __name__ == "__main__":
    load()
    while var.running:
        logged = False
        print("Pilih opsi :  ")
        print("(1) Login")
        print("(2) Help")
        print("(3) Exit")
        op = str(input("Input : "))
        if op.lower() == "login" or op == "1":
            userInfo = login(var.user)
            logged = True
        elif op.lower() == "help" or op == "2":
            help("")
        elif op.lower() == "exit" or op == "3":
            print()
            var.running = keluar()
        else:
            print()
        
        while logged:
            if userInfo[1] == "admin":
                print()
                print("+======== MAIN MENU =========+")
                func.drawTable([["Opsi"],["register"],["tambah_game"],["ubah_game"],["ubah_stok"],["list_game_toko"],["search_game_at_store"],["topup"],["help"],["save"],["logout"],["exit"]])
                op = str(input("Input : "))
                if op.lower() == "clear" or op.lower() == "0":
                    system('clear')
                elif op.lower() == "register" or op.lower() == "1":
                    register(var.user)
                elif op.lower() == "tambah_game" or op.lower() == "2":
                    addGame(var.game)
                elif op.lower() == "ubah_game" or op.lower() == "3":
                    changeAttr(var.game)
                elif op.lower() == "ubah_stok" or op.lower() == "4":
                    changeStock(var.game)
                elif op.lower() == "list_game_toko" or op.lower() == "5":
                    drawSortedMtx(var.game)
                elif op.lower() == "search_game_at_store" or op.lower() == "6":
                    search_game_at_store(var.game)
                elif op.lower() == "topup" or op.lower() == "7":
                    topup(var.user)
                elif op.lower() == "help" or op.lower() == "8":
                    help(userInfo[1])
                elif op.lower() == "save" or op.lower() == "9":
                    print()
                    save()
                elif op.lower() == "logout" or op.lower() == "10":
                    print()
                    func.loading("Logging out")
                    print()
                    logged = False
                elif op.lower() == "exit" or op.lower() == "11":
                    print()
                    var.running = keluar()
                    if var.running == False:
                        logged = False
                else: 
                    print()
                    print("Mohon memberi input sesuai pada menu di atas.")
            elif userInfo[1] == "user":
                print()
                print("+======== MAIN MENU =========+")
                func.drawTable([["Opsi"],["list_game_toko"],["buy_game"],["list_game"],["search_my_game"],["search_game_at_store"],["riwayat"],["extras"],["help"],["save"],["logout"],["exit"]])
                op = str(input("Input : "))
                if op.lower() == "clear" or op.lower() == "0":
                    system('clear')
                elif op.lower() == "list_game_toko" or op.lower() == "1":
                    drawSortedMtx(var.game)
                elif op.lower() == "buy_game" or op.lower() == "2":
                    buy_game(var.game, var.kepemilikan, var.user, var.riwayat, userInfo[0])
                elif op.lower() == "list_game" or op.lower() == "3":
                    list_game(var.game, var.kepemilikan, userInfo[0])
                elif op.lower() == "search_my_game" or op.lower() == "4":
                    search_my_game(var.game, var.kepemilikan, userInfo[0])
                elif op.lower() == "search_game_at_store" or op.lower() == "5":
                    search_game_at_store(var.game)
                elif op.lower() == "riwayat" or op.lower() == "6":
                    history(var.riwayat, userInfo[0])
                elif op.lower() == "extras" or op.lower() == "7":
                    cond = True
                    print()
                    print("Selamat datang di BNMO Game Center!")
                    while cond:
                        print()
                        print("Pilih opsi :")
                        print("(1) Magic Conch Shell")
                        print("(2) Tic Tac Toe")
                        print("(3) Back")
                        op2 = input("Input : ")
                        if op2.lower() == "magic conch shell" or op2 == "1":
                            mcs()
                        elif op2.lower() == "tic tac toe" or op2 == "2":
                            tictactoe()
                        elif op2.lower() == "back" or op2 == "3":
                            cond = False
                        else: print("Mohon memberi input sesuai pada menu di atas.")
                elif op.lower() == "help" or op.lower() == "8":
                    help(userInfo[1])
                elif op.lower() == "save" or op.lower() == "9":
                    print()
                    save()
                elif op.lower() == "logout" or op.lower() == "10":
                    print()
                    func.loading("Logging out")
                    print()
                    logged = False
                elif op.lower() == "exit" or op.lower() == "11":
                    print()
                    var.running = keluar()
                    if var.running == False:
                        logged = False
                else: 
                    print()
                    print("Mohon memberi input sesuai pada menu di atas.")