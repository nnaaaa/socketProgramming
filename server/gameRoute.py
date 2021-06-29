from userController import updatePoint

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
    targetMe = "You missed, no ship was shot 👎"
    targetEnemy = "Enemy missed, no ship was shot 👎"
    if primeMap[y][x] == "🌊":
        enemyMap[y][x] = "❌"
        blankMap[y][x] = "❌"
    else: 
        enemyMap[y][x] = "🎯"
        blankMap[y][x] = "🎯"
        targetMe = "You hit 🌋 !"
        targetEnemy = "Enemy hit 🌋 !"
        
        sign = primeMap[y][x]
        if isDestroyFullShip(blankMap,primeMap,sign):
            targetMe = "Enemy's ship was completely sunk 🚢 !!!"
            targetEnemy = "Enemy's ship was completely sunk 🚢 !!!"
            
            for i in range(0,10):
                for j in range(0,10):
                    if primeMap[i][j] == sign:
                        blankMap[i][j] = "✅"
                        enemyMap[i][j] = "✅"
    if isEndGame(primeMap,blankMap):
        targetMe = "🥇 Winner winner chicken dinner!!!"
        targetEnemy = "🤏 Loser!"
        updatePoint({"account":client["account"],"point":1000})
    
    clientRespond = {
        "map":blankMap,
        "target": targetMe,
    }
    enemyRespond = {
        "map":enemyMap,
        "target": targetEnemy,
    }
            

    client["socket"].send(bytes(str(clientRespond),'utf8'))
    enemy["socket"].send(bytes(str(enemyRespond),'utf8'))


def isDestroyFullShip(blankMap,primeMap,sign):
    for i in range(0,10):
        for j in range(0,10):
            if primeMap[i][j] == sign and blankMap[i][j] != "🎯":
                return False
    
    return True


def isEndGame(primeMap,blankMap):  
    for i in range(0,10):
        for j in range(0,10):
            if primeMap[i][j] != "🌊" and blankMap[i][j] != "✅":
                return False
    return True
    