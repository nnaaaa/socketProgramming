from userController import postLogin,postRegister,getUser,updateUser

def userRoute(client, data, usersOnline):
    if data["auth"] == "login":
        err = postLogin(data)
        # kiểm tra xem user đã đăng nhập chưa
        userOnline = list(filter(lambda item: item["account"] == data["account"], usersOnline))
        # nếu đã đăng nhập thì không cho đăng nhập nữa
        if len(userOnline) != 0:
            err["account"] = True
        
        # nếu không có lỗi gì thì thêm user vào danh sách online
        if not err["account"] and not err["password"]:
            client["account"] = data["account"]
            usersOnline.append(client)
        
        client["socket"].send(bytes(str(err), 'utf8'))

    elif data["auth"] == "register":
        err = postRegister(data)
        client["socket"].send(bytes(str(err),'utf8'))



    elif data["auth"] == "online":
        userOnline = list(filter(lambda item: item["account"] == data["account"],usersOnline))
        isOnline = False
        if len(userOnline) != 0 :
            isOnline = True
        client["socket"].send(bytes(str(isOnline),'utf8'))

    elif (data["auth"] == "find") or (data["auth"] == "show_fullname") or (data["auth"] == "show_note") or (data["auth"] == "show_point") or (data["auth"] == "show_all") or (data["auth"] == "show_date"):
        user = getUser(data)
        client["socket"].send(bytes(str(user),'utf8'))

    elif (data["auth"] == "setup_info") or  (data["auth"] == "changePassword"):
        updateUser(data)

    
