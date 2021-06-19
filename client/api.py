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