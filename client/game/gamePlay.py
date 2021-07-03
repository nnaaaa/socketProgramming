import ast
import pygame
import threading
from game.constants import *
from game.graphic import Atlas

def playerAttack(socket,myMap,account):
    blankMap = ast.literal_eval(socket.recv(9216).decode('utf8'))
    atlas = Atlas(socket,account,myMap,blankMap,False)
    threading.Thread(target=atlas.displayMap,args=(account,)).start()
    while atlas.playing:
        enemy = ast.literal_eval(socket.recv(9216).decode('utf8'))
        atlas.blankMap = enemy["map"]
        target = enemy["target"]
        if "Winner" in target or "Loser" in target:
            atlas.playing = False

        me = ast.literal_eval(socket.recv(9216).decode('utf8'))
        atlas.waiting = False
        atlas.myMap = me["map"]
        target = me["target"]
        if "Winner" in target or "Loser" in target:
            atlas.playing = False
     
        
def playerDefend(socket,myMap,account):
    blankMap = ast.literal_eval(socket.recv(9216).decode('utf8'))
    atlas = Atlas(socket,account,myMap,blankMap,True)
    threading.Thread(target=atlas.displayMap,args=(account,)).start()
    while atlas.playing:
        me = ast.literal_eval(socket.recv(9216).decode('utf8'))
        atlas.waiting = False
        atlas.myMap = me["map"]
        target = me["target"]
        if "Winner" in target or "Loser" in target:
            atlas.playing = False

        enemy = ast.literal_eval(socket.recv(9216).decode('utf8'))
        atlas.blankMap = enemy["map"]
        target = enemy["target"]
        if "Winner" in target or "Loser" in target:
            atlas.playing = False


