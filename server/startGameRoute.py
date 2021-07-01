water = "🌊"


def startGameRoute(client,data,usersOnline,enemy,myMap):
    if (data["game"] == "start_game"):
        accounts = list(map(lambda user: user["account"],usersOnline))
        client["socket"].send(bytes(str(accounts),'utf8'))

    elif(data["game"] == "create_room"):
        #2
        userOnline = list(filter(lambda user: user["account"] == data["account"],usersOnline))
        if len(userOnline) != 0:
            enemy["account"] = userOnline[0]["account"]
            enemy["socket"] = userOnline[0]["socket"]
        
            obj = {
                "game":"play-game",
                "account":client["account"],
                "challengerMap":data["challengerMap"]
            }
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
        enemy["socket"].send(bytes(str(obj),'utf8'))
        
    elif(data["game"] == "recv_enemy"):
        #4
        userOnline = list(filter(lambda user: user["account"] == data["account"],usersOnline))
        enemy["account"] = userOnline[0]["account"]
        enemy["socket"] = userOnline[0]["socket"]
       
        arr1 = []
        arr2 = []
        arr1 = copyMap(data["challengerMap"])
        arr2 = copyMap(data["challengerMap"])
        enemy["map"] = arr1
        enemy["primeMap"] = arr2
        createBlankMap(myMap)
        client["socket"].send(bytes(str(myMap),'utf8'))
        

    elif(data["game"] == "recv_map"):
        #8 
        arr1 = []
        arr2 = []
        arr1 = copyMap(data["accepterMap"])
        arr2 = copyMap(data["accepterMap"])
        enemy["map"] = arr1
        enemy["primeMap"] = arr2
        createBlankMap(myMap)
        client["socket"].send(bytes(str(myMap),'utf8'))



def copyMap(data):
    arr = []
    for i in range(0,10):
        clone = []
        for j in range(0,10):
            clone.append(data[i][j])
        arr.append(clone)
    return arr

def createBlankMap(Map):
    for i in range(0,10):
        arr = []
        for j in range(0,10):
            arr.append(water)
        Map.append(arr)


        





        
        
