import socket
import ast

def playerAttack(socket,account):
    playing = True 
    blankMap = ast.literal_eval(socket.recv(4096).decode('utf8'))
    while playing:
        print("🧩 Enemy Map ----------------------------------------")
        displayMap(blankMap)

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
        print(f"🎨 Your Map -----------------------------------------")
        displayMap(updatedMap)
        if "Winner" in target or "Loser" in target :
            break
        



def playerDefend(socket,account):
    playing = True 
    blankMap = ast.literal_eval(socket.recv(4096).decode('utf8'))
    while playing:
        print(f"⛳ Waiting for {account}'s attack...")
        me = ast.literal_eval(socket.recv(4096).decode('utf8'))
        updatedMap = me["map"]
        target = me["target"]
        print(target)
        print("🎨 Your Map -----------------------------------------")
        displayMap(updatedMap)
        if "Winner" in target or "Loser" in target:
            break
        print("🧩 Enemy Map ----------------------------------------")
        displayMap(blankMap)

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

def displayMap(mmap):
    for i in mmap:
        print(f"{i[0]} {i[1]} {i[2]} {i[3]} {i[4]} {i[5]} {i[6]} {i[7]} {i[8]} {i[9]}")

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

    if blankMap[y][x] == "🌊":
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

        if blankMap[y][x] == "🌊":
            isDuplicate = False
    
    return [int(chose[2]),int(chose[1])]

