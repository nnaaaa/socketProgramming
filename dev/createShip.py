import random
import time

sign = "."
tau27 = "X"
tau25 = "X"
tau14 = "X"
tau12 = "X"
tau11 = "X"


def taoMotTau(banDo,kichThuoc):
    chieuDoc = random.randint(0, 1)
    while True:
        if chieuDoc == 0:
            x = random.randint(0, 19 - kichThuoc["dai"] + 1)
            y = random.randint(0, 19 - kichThuoc["rong"] + 1)
            trungTau = xetTrungTau(banDo,kichThuoc,{"x":x,"y":y},chieuDoc)
            if not trungTau:
                taoTau(banDo, {"x":x,"y":y}, kichThuoc, chieuDoc)
                break

        elif chieuDoc == 1:
            x = random.randint(0, 19 - kichThuoc["rong"] + 1)
            y = random.randint(0, 19 - kichThuoc["dai"] + 1) 
            trungTau = xetTrungTau(banDo,kichThuoc,{"x":x,"y":y},chieuDoc)
            if not trungTau:
                taoTau(banDo, {"x":x,"y":y}, kichThuoc, chieuDoc)
                break


def taoTau(banDo,viTri,kichThuoc,chieuDoc):
    if chieuDoc:
        for i in range(viTri["x"],viTri["x"]+kichThuoc["rong"]):
            for j in range(viTri["y"],viTri["y"]+kichThuoc["dai"]):
                banDo[i][j] = xetKichThuoc(kichThuoc)
    if not chieuDoc:
        for i in range(viTri["x"],viTri["x"]+kichThuoc["dai"]):
            for j in range(viTri["y"],viTri["y"]+kichThuoc["rong"]):
                banDo[i][j] = xetKichThuoc(kichThuoc)

def xetTrungTau(banDo,kichThuoc,viTri,chieuDoc):
    if chieuDoc:
        for i in range(viTri["x"], viTri["x"] + kichThuoc["rong"]):
            for j in range(viTri["y"], viTri["y"] + kichThuoc["dai"]):
                if banDo[i][j] != sign:
                    return True

    if not chieuDoc:
        for i in range(viTri["x"], viTri["x"] + kichThuoc["dai"]):
            for j in range(viTri["y"], viTri["y"] + kichThuoc["rong"]):
                if banDo[i][j] != sign:
                    return True

    return False



def xetKichThuoc(kichThuoc):
    if kichThuoc["dai"]*kichThuoc["rong"] == 14:
        return tau27

    if kichThuoc["dai"]*kichThuoc["rong"] == 10:
        return tau25

    if kichThuoc["dai"]*kichThuoc["rong"] == 4:
        return tau14

    if kichThuoc["dai"]*kichThuoc["rong"] == 2:
        return tau12

    if kichThuoc["dai"]*kichThuoc["rong"] == 1:
        return tau11

    