import ast
def signin(userParams,socket):
    userParams["cmd"] = "login"
    # gửi tài khoản mật khẩu lên server
    socket.send(bytes(str(userParams),'utf8'))
    # server trả lỗi về
    err = ast.literal_eval(socket.recv(1024).decode('utf8'))
    # server trả về lỗi tài khoản
    if err["account"]:
        print("😩 Account doesn't exist")
        return False
    # server trả về lỗi mật khẩu
    elif err["password"]:
        print("😓 Wrong password")
        return False
    # server trả về lỗi rỗng
    else:  
        return True

def signup(userParams,socket):
    userParams["cmd"] = "register"
    # gửi tài khoản mật khẩu lên server
    socket.send(bytes(str(userParams),'utf8'))
    # server trả lỗi về
    err = ast.literal_eval(socket.recv(1024).decode('utf8'))
    # server trả về lỗi tài khoản 
    if err["account"]:
        print("😛 Account does exist")
        return False
    else:
        return True

def changePassword(userParams,socket):
    userParams["cmd"] = "changePassword"
    # gửi tài khoản mật khẩu mới lên server
    socket.send(bytes(str(userParams),'utf8'))
    
def checkUser(option,account,socket):
    obj = {
        "cmd":option,
        "account":account
    }
    if option == "find":
        socket.send(bytes(str(obj),'utf8'))
        exist = socket.recv(1024).decode('utf8')
        if exist == "True":
            print(f"🎁 {account} exist")
        else:
            print(f"🤷 {account} doesn't exist")
    # if option == "online":
    #     socket.send(bytes(f'{option} {userName}','utf8'))
    #     exist = ast.literal_eval(socket.recv(1024).decode('utf8'))
    # if option == "show_date":
    #     socket.send(bytes(f'{option} {userName}','utf8'))
    #     exist = ast.literal_eval(socket.recv(1024).decode('utf8'))
    # if option == "show_fullname":
    #     socket.send(bytes(f'{option} {userName}','utf8'))
    #     exist = ast.literal_eval(socket.recv(1024).decode('utf8'))
    # if option == "show_note":
    #     socket.send(bytes(f'{option} {userName}','utf8'))
    #     exist = ast.literal_eval(socket.recv(1024).decode('utf8'))
    # if option == "show_all":
    #     socket.send(bytes(f'{option} {userName}','utf8'))
    #     exist = ast.literal_eval(socket.recv(1024).decode('utf8'))
    # if option == "show_point":
    #     socket.send(bytes(f'{option} {userName}','utf8'))
    #     exist = ast.literal_eval(socket.recv(1024).decode('utf8'))

def setInfo(option,account,socket):
    if option == "fullname":
        fullName = input("")
        socket.send(bytes(f'{option} {fullName}','utf8'))
        exist = ast.literal_eval(socket.recv(1024).decode('utf8'))
