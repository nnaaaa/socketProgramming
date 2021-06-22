import socket
import ast
from userRoute import userRoute
from threading import Thread

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),8000))
s.listen(5)
print("😋 Server start")
usersOnline = []

def Client(client,account):
    while True:
        data = client.recv(1024)
        if not data :
            print(f"Client from {addr} disconnect")
            # xóa user khỏi danh sách online
            usersOnline.remove(account["me"])
            print("👉 listOnline:",usersOnline)
            #đóng kết nối với user
            client.close()
            break

        data = ast.literal_eval(data.decode('utf8'))

        if (data.get("auth")):
            userRoute(client,data,usersOnline,account)




while True:
    client,addr = s.accept()
    print(f"Client from {addr} connect")
    account = {}
    Thread(target=Client,args=(client,account)).start()
    

s.close()






        
