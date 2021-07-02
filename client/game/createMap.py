from game.createShip import taoMotTau
from game.constants import *
import pygame


def createMap(banDo):
    for i in range(0,Map["doc"]):
        arr = []
        for j in range(0,Map["ngang"]):
            arr.append("water") 
        banDo.append(arr)
    
    taoMotTau(banDo,kichThuoc27,"tau27")
    taoMotTau(banDo,kichThuoc25,"tau25")
    # taoMotTau(banDo,kichThuoc25,"Q")
    taoMotTau(banDo,kichThuoc14,"tau14")
    # taoMotTau(banDo,kichThuoc14,"9")
    # taoMotTau(banDo,kichThuoc14,"8")
    taoMotTau(banDo,kichThuoc12,"tau12")
    # taoMotTau(banDo,kichThuoc12,"6")
    # taoMotTau(banDo,kichThuoc12,"5")
    # taoMotTau(banDo,kichThuoc11,"4")
    # taoMotTau(banDo,kichThuoc11,"3")
    taoMotTau(banDo,kichThuoc11,"tau11")





