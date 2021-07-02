import ast
import pygame
from game.constants import *

atlas = {
    "blank":[],
    "updated":[],
    "playing":True,
    "waiting":True
}


def playerAttack(socket,myMap,account):
    playing = True 
    atlas["blank"] = ast.literal_eval(socket.recv(9216).decode('utf8'))
    atlas["updated"] = myMap
    while playing:
        print("🧩 Enemy Map ----------------------------------------")
        displayMap(blankMap)

        obj = {
            "attack":True,
            "position":{"x":x,"y":y}     
        }
        socket.send(bytes(str(obj),'utf8'))
        enemy = ast.literal_eval(socket.recv(9216).decode('utf8'))
        blankMap = enemy["map"]
        target = enemy["target"]
        print(target)
        if "Winner" in target or "Loser" in target :
            break

        print(f"⛳ Waiting for {account}'s attack...")
        me = ast.literal_eval(socket.recv(9216).decode('utf8'))
        updatedMap = me["map"]
        target = me["target"]

        print(target)
        if "Winner" in target or "Loser" in target :
            break
        print(f"🎨 Your Map -----------------------------------------")
        displayMap(updatedMap)
        #--------------------------------------------------------------
        
        
        



def playerDefend(socket,myMap,account):
    playing = True 
    atlas["blank"] = ast.literal_eval(socket.recv(9216).decode('utf8'))
    atlas["updated"] = myMap
    while playing:
        print(f"⛳ Waiting for {account}'s attack...")
        me = ast.literal_eval(socket.recv(9216).decode('utf8'))
        updatedMap = me["map"]
        target = me["target"]
        print(target)
        if "Winner" in target or "Loser" in target:
            break
        print("🎨 Your Map -----------------------------------------")
        displayMap(updatedMap)
        
        print("🧩 Enemy Map ----------------------------------------")
        displayMap(blankMap)

        x,y = checkInput(blankMap)
        obj = {
            "attack":True,
            "position":{"x":x,"y":y} 
        }
        socket.send(bytes(str(obj),'utf8'))
        enemy = ast.literal_eval(socket.recv(9216).decode('utf8'))
        blankMap = enemy["map"]
        target = enemy["target"]
        print(target)
        if "Winner" in target or "Loser" in target:
            break


def displayMap(enemyMap):

    for i in range(0,10):
        print(f"{enemyMap[i][0]} {enemyMap[i][1]} {enemyMap[i][2]} {enemyMap[i][3]} {enemyMap[i][4]} {enemyMap[i][5]} {enemyMap[i][6]} {enemyMap[i][7]} {enemyMap[i][8]} {enemyMap[i][9]}")




def handle_mouse_click(atlas,pos):
    for i in atlas:
        for j in i:
            if j["pos"][0] < pos[0] < j["pos"][0] + 30 and j["pos"][1] < pos[1] < j["pos"][1] + 30:
                j["sprite"] = pygame.transform.scale(pygame.image.load("assets/cancel.png"),(30,30))

