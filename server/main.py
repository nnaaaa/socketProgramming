import socket
import ast
from userRoute import userRoute
from gameRoute import gameRoute
from threading import Thread

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),8000))
s.listen(5)
print("😋 Server start")
usersOnline = []
# {"socket":,"account":"..."}

def Client(client,address):
    enemy = {}
    
    while True:
        data = client["socket"].recv(4096)
        if not data :
            print(f"Client from {address} disconnect")
            # xóa user khỏi danh sách online

            usersOnline.remove({
                "account":client["account"],
                "socket":client["socket"]
            })
            #đóng kết nối với user
            client["socket"].close()
            break

        data = ast.literal_eval(data.decode('utf8'))
        
        if (data.get("auth")):
            userRoute(client,data,usersOnline)

        if (data.get("game")):
            gameRoute(client,data,usersOnline,enemy)




while True:
    socketClient,address = s.accept()
    print(f"Client from {address} connect")
    client = {"socket":socketClient}
    Thread(target=Client,args=(client,address)).start()
    

s.close()






        
