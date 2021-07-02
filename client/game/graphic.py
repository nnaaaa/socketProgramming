import ast
import pygame
import threading
from game.constants import *



atlas = {
    "blank":[],
    "updated":[],
    "playing":True,
    "waiting":True
}

def playerAttack(socket,myMap,account):
    atlas["blank"] = ast.literal_eval(socket.recv(9216).decode('utf8'))
    atlas["updated"] = myMap 
    atlas["waiting"] = False
    threading.Thread(target=displayMap,args=(socket,account)).start()
    while atlas["playing"]:
        enemy = ast.literal_eval(socket.recv(9216).decode('utf8'))
        atlas["blank"] = enemy["map"]
        target = enemy["target"]
        if "Winner" in target or "Loser" in target:
            atlas["playing"] = False

        me = ast.literal_eval(socket.recv(9216).decode('utf8'))
        atlas["waiting"] = False
        atlas["updated"] = me["map"]
        target = me["target"]
        if "Winner" in target or "Loser" in target:
            atlas["playing"] = False
        #--------------------------------------------------------------

        
        
def playerDefend(socket,myMap,account):
    atlas["blank"] = ast.literal_eval(socket.recv(9216).decode('utf8'))
    atlas["updated"] = myMap 
    atlas["waiting"] = True
    threading.Thread(target=displayMap,args=(socket,account)).start()
    while atlas["playing"]:
        me = ast.literal_eval(socket.recv(9216).decode('utf8'))
        atlas["waiting"] = False
        atlas["updated"] = me["map"]
        target = me["target"]
        if "Winner" in target or "Loser" in target:
            atlas["playing"] = False

        enemy = ast.literal_eval(socket.recv(9216).decode('utf8'))
        atlas["blank"] = enemy["map"]
        target = enemy["target"]
        if "Winner" in target or "Loser" in target:
            atlas["playing"] = False

def displayMap(socket,account):
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((32*20, 32*20))
    pygame.display.set_caption("Battle Ship")
    icon = pygame.image.load("client/game/assets/battleship.png")
    pygame.display.set_icon(icon)
    while atlas["playing"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                atlas["playing"] = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                onClick(socket,pos)

        screen.fill((18, 66, 129))
        for i in range(0,20):
            for j in range(0,20):
                if atlas["blank"][i][j] == "water":
                    screen.blit(water, (j*32,i*32))
                if atlas["blank"][i][j] == "hit":
                    screen.blit(hit, (j*32,i*32))
                if atlas["blank"][i][j] == "full":
                    screen.blit(full, (j*32,i*32))
                if atlas["blank"][i][j] == "missed":
                    screen.blit(missed, (j*32,i*32))
                if "ship" in atlas["blank"][i][j]:
                    screen.blit(ship1, (j*32,i*32))
        pygame.display.update()
    pygame.display.flip()

def onClick(socket,pos):
    if atlas["waiting"]:
        return
    for i in range(0,20):
        for j in range(0,20):
            if j*32 < pos[1] < j*32 + 30 and i*32 < pos[0] < i*32 + 30:
                if atlas["blank"][i][j] == "water":
                    obj = {
                        "attack":True,
                        "position":{"x":i,"y":j} 
                    }
                    print("i:",i,"  j:",j)
                    atlas["waiting"] = True
                    socket.send(bytes(str(obj),'utf8'))

