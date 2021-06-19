import socket
import ast
from userController import postLogin,postRegister,updatePassword
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('0.0.0.0',8000))
s.listen(5)

while True:
    client,addr = s.accept()
    print(f"Client from {addr} connect")
    while True:
        data = client.recv(1024)
        data = ast.literal_eval(data.decode('utf8'))
        if data["cmd"] == "login":
            err = postLogin(data)
            client.send(bytes(str(err),'utf8'))
        elif data["cmd"] == "register":
            err = postRegister(data)
            client.send(bytes(str(err),'utf8'))
        elif data["cmd"] == "changePassword":
            updatePassword(data)
    client.close()
s.close()



        
