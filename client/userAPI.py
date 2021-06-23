import ast
def signin(userParams,socket):
    userParams["auth"] = "login"
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
    userParams["auth"] = "register"
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
    userParams["auth"] = "changePassword"
    # gửi tài khoản mật khẩu mới lên server
    socket.send(bytes(str(userParams),'utf8'))
    
def checkUser(option,account,socket):
    obj = {
        "auth":option,
        "account":account
    }
    if option == "find":
        socket.send(bytes(str(obj),'utf8'))
        user = ast.literal_eval(socket.recv(1024).decode('utf8'))
        if user == "False":
            print(f"🤷 {account} doesn't exist")
        else:
            print(f"🥽 {account} exist")
    if option == "online":
        socket.send(bytes(str(obj),'utf8'))
        isOnline = socket.recv(1024).decode('utf8')
        if isOnline == "False":
            print(f"🎃 User is offline")
        else:
            print(f"🎨 User is online")
    if option == "show_date":
        socket.send(bytes(str(obj),'utf8'))
        user = ast.literal_eval(socket.recv(1024).decode('utf8'))
        if user == "False":
            print(f"📆 Birthday of {account} is " + user["birthday"])
        else: 
            print(f"🤷 {account} doesn't exist")
    if option == "show_fullname":
        socket.send(bytes(str(obj),'utf8'))
        user = ast.literal_eval(socket.recv(1024).decode('utf8'))
        if user == "False":
            print(f"🤷 {account} doesn't exist")
        if "fullname" in user:
            print(f"🎩 Fullname of {account} is " + user["fullname"])
        else: 
            print(f"🍗 Fullname doesn't setup")
    if option == "show_note":
        socket.send(bytes(str(obj),'utf8'))
        user = ast.literal_eval(socket.recv(1024).decode('utf8'))
        if user == "False":
            print(f"🤷 {account} doesn't exist")
        if "note" in user:
            print(f"📖 Note: " + user["note"])
        else: 
            print(f"🍗 Note doesn't setup")
    if option == "show_all":
        socket.send(bytes(str(obj),'utf8'))
        user = ast.literal_eval(socket.recv(1024).decode('utf8'))
        if user == "False":
            print(f"🤷 {account} doesn't exist")
        else: 
            # lấy password ra trước khi in tất cả thông tin
            user.pop("password")
            for i in user.keys():
                print(f"💎 {i}: " + str(user[i]))
    if option == "show_point":
        socket.send(bytes(str(obj),'utf8'))
        user = ast.literal_eval(socket.recv(1024).decode('utf8'))
        if user == "False":
            print(f"🤷 {account} doesn't exist")
        else: 
            print(f"🎯 Point of {account} is " + str(user["point"]))

def setInfo(option,string,account,socket):
    obj = {
        "auth":"setup_info",
        option:string,
        "account":account
    }
    if option != "date" and option != "note" and option != "fullname":
        print("💔 Can't set this information")
        return
    socket.send(bytes(str(obj),'utf8'))
    print(f"🎉 {option} of {account} is {string}")


