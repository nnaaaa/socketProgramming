import ast

def startGameRoute(client,data,usersOnline,enemy):
    if (data["game"] == "start_game"):
        accounts = list(map(lambda user: user["account"],usersOnline))
        client["socket"].send(bytes(str(accounts),'utf8'))

    elif(data["game"] == "create_room"):
        userOnline = list(filter(lambda user: user["account"] == data["account"],usersOnline))
        #enemy la thang
        enemy["account"] = userOnline[0]["account"]
        enemy["socket"] = userOnline[0]["socket"]
        
        obj = {
            "game":"play-game",
            "account":client["account"],
            "challengerMap":data["myMap"]
        }
        #duc
        userOnline[0]["socket"].send(bytes(str(obj),'utf8'))
        
        
    elif(data["game"] == "send_map"):
        obj = {
            "game":"send_map",
            "map":data["map"]
        }
        #thang
        enemy["socket"].send(bytes(str(obj),'utf8'))
        
    elif(data["game"] == "recv_enemy"):
        userOnline = list(filter(lambda user: user["account"] == data["account"],usersOnline))
        enemy["account"] = userOnline[0]["account"]
        enemy["socket"] = userOnline[0]["socket"]
        enemy["map"] = data["challengerMap"]
        print("client:",client["account"])
        for i in range(0,20):
            print(enemy["map"][i])
            
    elif(data["game"] == "recv_map"):
        enemy["map"] = data["challengerMap"]
        print("client:",client["account"])
        for i in range(0,20):
            print(enemy["map"][i])


        





        
        
