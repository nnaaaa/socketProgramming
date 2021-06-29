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
                "challengerMap":data["challengerMap"]
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
            "accepterMap":data["accepterMap"]
        }
        #thang
        enemy["socket"].send(bytes(str(obj),'utf8'))
        
    elif(data["game"] == "recv_enemy"):
        #4
        userOnline = list(filter(lambda user: user["account"] == data["account"],usersOnline))
        enemy["account"] = userOnline[0]["account"]
        enemy["socket"] = userOnline[0]["socket"]
       
        arr1 = []
        arr2 = []
        for i in range(0,10):
            b1 = []
            b2 = []
            for j in range(0,10):
                b1.append(data["challengerMap"][i][j])
                b2.append(data["challengerMap"][i][j])
            arr1.append(b1)
            arr2.append(b2)

        enemy["map"] = arr1
        enemy["primeMap"] = arr2


        for i in range(0,10):
            arr = []
            for j in range(0,10):
                arr.append(".")
            myMap.append(arr)
        client["socket"].send(bytes(str(myMap),'utf8'))
        

    elif(data["game"] == "recv_map"):
        #8 
        arr1 = []
        arr2 = []
        for i in range(0,10):
            b1 = []
            b2 = []
            for j in range(0,10):
                b1.append(data["accepterMap"][i][j])
                b2.append(data["accepterMap"][i][j])
            arr1.append(b1)
            arr2.append(b2)

        enemy["map"] = arr1
        enemy["primeMap"] = arr2

        
        for i in range(0,10):
            arr = []
            for j in range(0,10):
                arr.append(".")
            myMap.append(arr)
        client["socket"].send(bytes(str(myMap),'utf8'))



        





        
        
