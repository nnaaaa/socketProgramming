from game.createShip import taoMotTau
from game.constants import *

def createMap(banDo):
    for i in range(0,Map["doc"]):
        arr = []
        for j in range(0,Map["ngang"]):
            arr.append("water") 
        banDo.append(arr)
    
    taoMotTau(banDo,kichThuoc27,"ship12")
    taoMotTau(banDo,kichThuoc25,"ship11")
    taoMotTau(banDo,kichThuoc25,"ship10")
    taoMotTau(banDo,kichThuoc14,"ship9")
    taoMotTau(banDo,kichThuoc14,"ship8")
    taoMotTau(banDo,kichThuoc14,"ship7")
    taoMotTau(banDo,kichThuoc12,"ship6")
    taoMotTau(banDo,kichThuoc12,"ship5")
    taoMotTau(banDo,kichThuoc12,"ship4")
    taoMotTau(banDo,kichThuoc11,"ship3")
    taoMotTau(banDo,kichThuoc11,"ship2")
    taoMotTau(banDo,kichThuoc11,"ship1")





