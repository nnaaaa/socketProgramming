import ast
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
        atlas.status = enemy["target"]
        if "Winner" in atlas.status or "Loser" in atlas.status:
            print(atlas.status)
            atlas.playing = False
            break

        me = ast.literal_eval(socket.recv(9216).decode('utf8'))
        atlas.waiting = False
        atlas.myMap = me["map"]
        atlas.status = me["target"]
        if "Winner" in atlas.status or "Loser" in atlas.status:
            print(atlas.status)
            atlas.playing = False
            break
    del atlas
        
def playerDefend(socket,myMap,account):
    blankMap = ast.literal_eval(socket.recv(9216).decode('utf8'))
    atlas = Atlas(socket,account,myMap,blankMap,True)
    threading.Thread(target=atlas.displayMap,args=(account,)).start()
    while atlas.playing:
        me = ast.literal_eval(socket.recv(9216).decode('utf8'))
        atlas.waiting = False
        atlas.myMap = me["map"]
        atlas.status = me["target"]
        if "Winner" in atlas.status or "Loser" in atlas.status:
            print(atlas.status)
            atlas.playing = False
            break

        enemy = ast.literal_eval(socket.recv(9216).decode('utf8'))
        atlas.blankMap = enemy["map"]
        atlas.status = enemy["target"]
        if "Winner" in atlas.status or "Loser" in atlas.status:
            print(atlas.status)
            atlas.playing = False
            break
    del atlas

