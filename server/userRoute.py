from userController import postLogin,postRegister,getUser,updateUser

def userRoute(client, data, usersOnline,account):
    if data["auth"] == "login":
        
        err = postLogin(data)
        # kiểm tra xem user đã đăng nhập chưa
        isOnline = list(filter(lambda item: item ==
                        data["account"], usersOnline))
        # nếu đã đăng nhập thì không cho đăng nhập nữa
        if len(isOnline) != 0:
            err["account"] = True
        
        # nếu không có lỗi gì thì thêm user vào danh sách online
        if not err["account"] and not err["password"]:
            usersOnline.append(data["account"])
            account["me"] = data["account"]
            print("👉 listOnline:", usersOnline)
        
        client.send(bytes(str(err), 'utf8'))

    elif data["auth"] == "register":
        err = postRegister(data)
        client.send(bytes(str(err),'utf8'))

    elif data["auth"] == "online":
        userOnline = list(filter(lambda item: item == data["account"],usersOnline))
        isOnline = False
        if len(userOnline) != 0 :
            isOnline = True
        client.send(bytes(str(isOnline),'utf8'))

    elif (data["auth"] == "find") or (data["auth"] == "show_fullname") or (data["auth"] == "show_note") or (data["auth"] == "show_point") or (data["auth"] == "show_all") or (data["auth"] == "show_date"):
        user = getUser(data)
        client.send(bytes(str(user),'utf8'))

    elif (data["auth"] == "setup_info") or  (data["auth"] == "changePassword"):
        updateUser(data)

    
