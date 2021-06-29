def attackRoute(client, data, enemy,blankMap):
    x = data["position"]["x"] - 1
    y = data["position"]["y"] - 1
    primeMap = enemy["primeMap"]
    enemyMap = enemy["map"]
    """
    1. "." = water or empty space
    2. "O" = full ship that was hit with bullet
    3. "X" = part of ship that was hit with bullet
    4. "#" = water that was shot with bullet, a miss because it hit no ship
    """
    if primeMap[y][x] == ".":
        enemyMap[y][x] = "#"
        blankMap[y][x] = "#"
    else: 
        enemyMap[y][x] = "X"
        blankMap[y][x] = "X"
        sign = primeMap[y][x]
        print(sign)
        if isDestroyFullShip(blankMap,primeMap,sign):
            for i in range(0,10):
                for j in range(0,10):
                    if primeMap[i][j] == sign:
                        blankMap[i][j] = "O"
                        enemyMap[i][j] = "O"

    client["socket"].send(bytes(str(blankMap),'utf8'))
    enemy["socket"].send(bytes(str(enemyMap),'utf8'))


def isDestroyFullShip(blankMap,primeMap,sign):
    for i in range(0,10):
        for j in range(0,10):
            if primeMap[i][j] == sign and blankMap[i][j] != "X":
                return False
    
    return True








