import socket
import ast
from userController import postLogin,postRegister,getUser,updateUser
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('0.0.0.0',8000))
s.listen(5)

usersOnline = []

while True:
    client,addr = s.accept()
    print(f"Client from {addr} connect")
    account = ""
    while True:
        data = client.recv(1024)
        
        if not data :
            print(f"Client from {addr} disconnect")
            usersOnline.remove(account)
            print("👉 listOnline:",usersOnline)
            client.close()
            break

        data = ast.literal_eval(data.decode('utf8'))

        if data["cmd"] == "login":
            err = postLogin(data)
            # kiểm tra xem user đã đăng nhập chưa
            isOnline = list(filter(lambda item: item == data["account"],usersOnline))
            if not err["account"] and not err["password"]:
                usersOnline.append(data["account"])
                account = data["account"]
                print("👉 listOnline:",usersOnline)
            # nếu đã đăng nhập thì không cho đăng nhập nữa
            if len(isOnline) != 0 :
                err["account"] == True
            client.send(bytes(str(err),'utf8'))

        elif data["cmd"] == "register":
            err = postRegister(data)
            client.send(bytes(str(err),'utf8'))

        elif data["cmd"] == "online":
            userOnline = list(filter(lambda item: item == data["account"],usersOnline))
            isOnline = False
            if len(userOnline) != 0 :
                isOnline = True
            client.send(bytes(str(isOnline),'utf8'))

        elif (data["cmd"] == "find") or (data["cmd"] == "show_fullname") or (data["cmd"] == "show_note") or (data["cmd"] == "show_point") or (data["cmd"] == "show_all") or (data["cmd"] == "show_date"):
            user = getUser(data)
            client.send(bytes(str(user),'utf8'))

        elif (data["cmd"] == "setup_info") or  (data["cmd"] == "changePassword"):
            updateUser(data)

s.close()



        
