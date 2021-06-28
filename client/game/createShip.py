import random

Map = {
    "ngang":20,
    "doc":20
}
water = "."
kichThuoc27 = {"dai":7,"rong":2}
kichThuoc25 = {"dai":5,"rong":2}
kichThuoc14 = {"dai":4,"rong":1}
kichThuoc12 = {"dai":2,"rong":1}
kichThuoc11 = {"dai":1,"rong":1}

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
                if banDo[i][j] != water:
                    return True

    if not chieuDoc:
        for i in range(viTri["x"], viTri["x"] + kichThuoc["dai"]):
            for j in range(viTri["y"], viTri["y"] + kichThuoc["rong"]):
                if banDo[i][j] != water:
                    return True

    return False



# def xetKichThuoc(kichThuoc):
#     if kichThuoc["dai"]*kichThuoc["rong"] == 14:
#         return tau27

#     if kichThuoc["dai"]*kichThuoc["rong"] == 10:
#         return tau25

#     if kichThuoc["dai"]*kichThuoc["rong"] == 4:
#         return tau14

#     if kichThuoc["dai"]*kichThuoc["rong"] == 2:
#         return tau12

#     if kichThuoc["dai"]*kichThuoc["rong"] == 1:
#         return tau11

    