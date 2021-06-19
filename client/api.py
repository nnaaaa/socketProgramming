import ast
def signin(userParams,socket):
    userParams["cmd"] = "login"
    socket.send(bytes(str(userParams),'utf8'))
    err = ast.literal_eval(socket.recv(1024).decode('utf8'))
    if err["account"]:
        print("😩 Account doesn't exist")
        return False
    elif err["password"]:
        print("😓 Wrong password")
        return False
    else:  
        return True

def signup(userParams,socket):
    userParams["cmd"] = "register"
    socket.send(bytes(str(userParams),'utf8'))
    err = ast.literal_eval(socket.recv(1024).decode('utf8'))
    if err["account"]:
        print("😛 Account does exist")
        return False
    else:
        return True