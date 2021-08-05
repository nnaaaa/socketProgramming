import socket
import ast
from userRoute import userRoute
from startGameRoute import startGameRoute
from gameRoute import attackRoute
from threading import Thread
# from gameRoute import 

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('26.69.245.250',8000))
s.listen(5)
print("😋 Server start at 26.69.246.14:8000")
usersOnline = []
# {"socket":,"account":"..."}

def Client(client,address):
    enemy = {}
    myMap = []
    while True:
        data = client["socket"].recv(9216)
        if not data:
            print(f"Client from {address} disconnect")
            # xóa user khỏi danh sách online
            if client["login"]:
                usersOnline.remove({
                    "account":client["account"],
                    "socket":client["socket"],
                    "login":client["login"]
                })
            #đóng kết nối với user
            client["socket"].close()
            break

        data = ast.literal_eval(data.decode('utf8'))

        # print("data:",data)

        if (data.get("auth")):
            userRoute(client,data,usersOnline)

        if (data.get("game")):
            startGameRoute(client,data,usersOnline,enemy,myMap)

        if (data.get("attack")):
            attackRoute(client, data, enemy,myMap)


while True:
    socketClient,address = s.accept()
    print(f"Client from {address} connect")
    client = {"socket":socketClient,"login":False}
    Thread(target=Client,args=(client,address)).start()
    
s.close()






        
