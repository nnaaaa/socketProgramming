import random
from game.constants import *


def taoMotTau(banDo,kichThuoc,sign):
    while True:
        chieuDoc = random.randint(0, 1)
        if chieuDoc == 0:
            x = random.randint(0, Map["ngang"] - kichThuoc["dai"])
            y = random.randint(0, Map["ngang"] - kichThuoc["rong"])
            trungTau = xetTrungTau(banDo,kichThuoc,{"x":x,"y":y},chieuDoc)
            if not trungTau:
                taoTau(banDo, {"x":x,"y":y}, kichThuoc, chieuDoc, sign)
                break

        elif chieuDoc == 1:
            x = random.randint(0, Map["ngang"] - kichThuoc["rong"])
            y = random.randint(0, Map["doc"] - kichThuoc["dai"]) 
            trungTau = xetTrungTau(banDo,kichThuoc,{"x":x,"y":y},chieuDoc)
            if not trungTau:
                taoTau(banDo, {"x":x,"y":y}, kichThuoc, chieuDoc,sign)
                break


def taoTau(banDo,viTri,kichThuoc,chieuDoc,sign):
    if chieuDoc:
        for i in range(viTri["x"],viTri["x"]+kichThuoc["rong"]):
            for j in range(viTri["y"],viTri["y"]+kichThuoc["dai"]):
                banDo[i][j] = sign


    if not chieuDoc:
        for i in range(viTri["x"],viTri["x"]+kichThuoc["dai"]):
            for j in range(viTri["y"],viTri["y"]+kichThuoc["rong"]):
                banDo[i][j] = sign



def xetTrungTau(banDo,kichThuoc,viTri,chieuDoc):
    if chieuDoc:
        for i in range(viTri["x"], viTri["x"] + kichThuoc["rong"]):
            for j in range(viTri["y"], viTri["y"] + kichThuoc["dai"]):
                if banDo[i][j] != "water":
                    return True

    if not chieuDoc:
        for i in range(viTri["x"], viTri["x"] + kichThuoc["dai"]):
            for j in range(viTri["y"], viTri["y"] + kichThuoc["rong"]):
                if banDo[i][j] != "water":
                    return True

    return False

