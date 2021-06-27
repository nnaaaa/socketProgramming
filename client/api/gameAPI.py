import ast
from game.createMap import createMap

def getUsersOnline(socket):
    obj = {"game":"start_game"}
    socket.send(bytes(str(obj),'utf8'))
    listUsers = ast.literal_eval(socket.recv(4096).decode('utf8'))
    return listUsers

def createRoom(option,room,account,socket):
    client1Map = []
    createMap(client1Map)
    obj={
        "game":option,
        "room":room,
        "account":account,
        "myMap":client1Map
    }
    socket.send(bytes(str(obj),'utf8'))
    enemy = ast.literal_eval(socket.recv(4096).decode('utf8'))
    obj={
        "game":"recv_map",
        "challengerMap":enemy["map"]
    }
    socket.send(bytes(str(obj),'utf8'))
    print("Start game!")


def waiting(socket):
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

            socket.send(bytes(str(obj),'utf8'))
        #     dataMap = ast.literal_eval(socket.recv(4096).decode('utf8'))
        #     obj = {
        #         "game":"recv_map",
        #         "map":dataMap
        #     }
        #     socket.send(bytes(str(obj),'utf8'))
            
        #     print("Start game!!!!!!")
        # elif chose == "N":
        #     socket.send(bytes(str({"concho":"conchoNguyenThang-xoa_du_ma_ccount_NguyenThang"}),'utf8'))


    
