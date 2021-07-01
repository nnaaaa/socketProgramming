import ast
from game.constants import *

def playerAttack(socket,account):
    playing = True 
    blankMap = ast.literal_eval(socket.recv(4096).decode('utf8'))
    while playing:
        print("🧩 Enemy Map ----------------------------------------")
        displayMap(updatedMap,blankMap,f)

        x,y = checkInput(blankMap)
        obj = {
            "attack":True,
            "position":{"x":x,"y":y}     
        }
        socket.send(bytes(str(obj),'utf8'))
        enemy = ast.literal_eval(socket.recv(4096).decode('utf8'))
        blankMap = enemy["map"]
        target = enemy["target"]
        print(target)
        if "Winner" in target or "Loser" in target :
            break

        print(f"⛳ Waiting for {account}'s attack...")
        me = ast.literal_eval(socket.recv(4096).decode('utf8'))
        updatedMap = me["map"]
        target = me["target"]

        print(target)
        if "Winner" in target or "Loser" in target :
            break
        print(f"🎨 Your Map -----------------------------------------")
        displayMap(updatedMap,blankMap,f)

        
        



def playerDefend(socket,account):
    playing = True 
    blankMap = ast.literal_eval(socket.recv(4096).decode('utf8'))
    f = open("client/game/viTriTau.txt","w")
    while playing:
        print(f"⛳ Waiting for {account}'s attack...")
        me = ast.literal_eval(socket.recv(4096).decode('utf8'))
        updatedMap = me["map"]
        target = me["target"]
        print(target)
        if "Winner" in target or "Loser" in target:
            break
        print("🎨 Your Map -----------------------------------------")
        displayMap(updatedMap,blankMap,f)
        
        print("🧩 Enemy Map ----------------------------------------")
        displayMap(updatedMap,blankMap,f)

        x,y = checkInput(blankMap)
        obj = {
            "attack":True,
            "position":{"x":x,"y":y} 
        }
        socket.send(bytes(str(obj),'utf8'))
        enemy = ast.literal_eval(socket.recv(4096).decode('utf8'))
        blankMap = enemy["map"]
        target = enemy["target"]
        print(target)
        if "Winner" in target or "Loser" in target:
            break

def displayMap(enemyMap,blankMap,f):
    for i in range(0,10):
        f.write(f"{enemyMap[i][0]} {enemyMap[i][1]} {enemyMap[i][2]} {enemyMap[i][3]} {enemyMap[i][4]} {enemyMap[i][5]} {enemyMap[i][6]} {enemyMap[i][7]} {enemyMap[i][8]} {enemyMap[i][9]}       {blankMap[i][0]} {blankMap[i][1]} {blankMap[i][2]} {blankMap[i][3]} {blankMap[i][4]} {blankMap[i][5]} {blankMap[i][6]} {blankMap[i][7]} {blankMap[i][8]} {blankMap[i][9]}")

def checkInput(blankMap):
    isDuplicate = True
    isFailSyntax = True
    commandline = input("🎮 This is your turn (y,x): ") 
    chose = commandline.split(" ")
    y = 1
    x = 1
    if commandline != "":
        if len(chose) == 3 and chose[0] == "attack":
            isFailSyntax = False
            y = int(chose[1]) - 1
            x = int(chose[2]) - 1
            if not 0 <= y < 10 or not 0 <= x < 10:
                isFailSyntax = True

    if blankMap[y][x] == water:
        isDuplicate = False

    
    while isDuplicate or isFailSyntax:
        print("🤮 You have chosen this position")
        commandline = input("👉 Please chose again (y,x): ") 
        chose = commandline.split(" ")
        if commandline != "":
            if len(chose) == 3 and chose[0] == "attack":
                isFailSyntax = False
                y = int(chose[1]) - 1
                x = int(chose[2]) - 1
                if not 0 <= y < 10 or not 0 <= x < 10:
                    isFailSyntax = True

        if blankMap[y][x] == water:
            isDuplicate = False
    
    return [int(chose[2]),int(chose[1])]

