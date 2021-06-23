def gameRoute(client,data,usersOnline):
    if (data["game"] == "start_game"):
        accounts = list(map(lambda user: user["account"],usersOnline))
        client["socket"].send(bytes(str(accounts),'utf8'))

    if(data["game"] == "create_room"):
        userOnline = list(filter(lambda user: user["account"] == data["account"],usersOnline))
        # user này không online
        respond = {
            "err":"",
        }
        if len(userOnline) != 0 :
            respond["err"] = "User doesn't online"
            client["socket"].send(bytes(str(respond),'utf8'))
        
