def attackRoute(client, data, enemy,blankMap):
    x = data["position"]["x"] - 1
    y = data["position"]["y"] - 1
    enemyMap = enemy["map"]
    #enemy={
    # "socket","map","account"
    # }

    """
    1. "." = water or empty space
    2. "O" = full ship that was hit with bullet
    3. "X" = part of ship that was hit with bullet
    4. "#" = water that was shot with bullet, a miss because it hit no ship

    
    """


    if enemyMap[y][x] == ".":
        blankMap[y][x] = "#"
    else: 
        blankMap[y][x] = "X"
        sign = enemyMap[y][x]
        if isDestroyFullShip(blankMap,enemyMap,sign):
            for i in range(0,20):
                for j in range(0,20):
                    if enemyMap[i][j] == sign:
                        blankMap[i][j] = "O"

    client["socket"].send(bytes(str(blankMap),'utf8'))
    enemy["socket"].send()





def findFullShip(enemyMap,sign):
    pos = []
    for i in range(0,20):
        for j in range(0,20):
            if enemyMap[i][j] == sign:
                pos.append({"y":i,"x":j})
    return pos
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
def isDestroyFullShip(blankMap,enemyMap,sign):
    fullShip = findFullShip(enemyMap,sign)
    for position in fullShip:
        if blankMap[position["y"]][position["x"]] != "X":
            return False 
    return True
