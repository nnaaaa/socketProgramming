import ast

def startGameRoute(client,data,usersOnline,enemy,myMap):
    if (data["game"] == "start_game"):
        accounts = list(map(lambda user: user["account"],usersOnline))
        client["socket"].send(bytes(str(accounts),'utf8'))

    elif(data["game"] == "create_room"):
        #2
        userOnline = list(filter(lambda user: user["account"] == data["account"],usersOnline))
        #enemy la thang
        if len(userOnline) != 0:
            enemy["account"] = userOnline[0]["account"]
            enemy["socket"] = userOnline[0]["socket"]
        
            obj = {
                "game":"play-game",
                "account":client["account"],
                "challengerMap":data["myMap"]
            }
            #duc
            enemy["socket"].send(bytes(str(obj),'utf8'))
        else:
            obj = {
                "game":"send_map_error",
            }
            client["socket"].send(bytes(str(obj),'utf8'))
        
        
    elif(data["game"] == "send_map"):
        #6
        obj = {
            "game":"send_map",
            "map":data["map"]
        }
        #thang
        enemy["socket"].send(bytes(str(obj),'utf8'))
        
    elif(data["game"] == "recv_enemy"):
        #4
        userOnline = list(filter(lambda user: user["account"] == data["account"],usersOnline))
        enemy["account"] = userOnline[0]["account"]
        enemy["socket"] = userOnline[0]["socket"]
        enemy["map"] = data["challengerMap"].copy()
        enemy["creMap"] = data["challengerMap"].copy()

        for i in range(0,20):
            arr = []
            for j in range(0,20):
                arr.append(".")
            myMap.append(arr)

    elif(data["game"] == "recv_map"):
        #8 
        enemy["map"] = data["challengerMap"].copy()
        enemy["creMap"] = data["challengerMap"].copy()
        for i in range(0,20):
            arr = []
            for j in range(0,20):
                arr.append(".")
            myMap.append(arr)


        





        
        
