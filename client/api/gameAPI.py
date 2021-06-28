import ast
from game.createMap import createMap
import game.gamePlay

def getUsersOnline(socket):
    obj = {"game":"start_game"}
    socket.send(bytes(str(obj),'utf8'))
    listUsers = ast.literal_eval(socket.recv(4096).decode('utf8'))
    return listUsers

def createRoom(option,room,account,socket):
    client1Map = []

    #1
    createMap(client1Map)
    obj={
        "game":option,
        "room":room,
        "account":account,
        "myMap":client1Map
    }
    socket.send(bytes(str(obj),'utf8'))

    #7
    enemy = ast.literal_eval(socket.recv(4096).decode('utf8'))
    if enemy["game"] == "send_map_error":
        print("😪 Fail to invite")
    else:
        obj={
            "game":"recv_map",
            "challengerMap":enemy["map"]
        }
        socket.send(bytes(str(obj),'utf8'))
        print("Start game!")
        #while loop game
        player1_attack(socket, account)



def waiting(socket):
    #3
    enemy = ast.literal_eval(socket.recv(4096).decode('utf8'))
    if 'play-game' in enemy["game"]:
        print("😍 " + enemy["account"] + " invite you ")
        chose = input(f"Do you want to play [Y/N] ")
        if chose == "Y":
            print("Start game!")
            obj = {
                "game":"recv_enemy",
                "account":enemy["account"],
                "challengerMap":enemy["challengerMap"]
            }
            socket.send(bytes(str(obj),'utf8'))
            
            client2Map = []
            createMap(client2Map)

            obj ={
                "game":"send_map",
                "map":client2Map
            }
            #5
            socket.send(bytes(str(obj),'utf8'))

            playing = True
            while playing:
                player2_defend                
                
       


    

