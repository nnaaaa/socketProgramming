from game.createShip import Map,taoMotTau,sign,kichThuoc27,kichThuoc25,kichThuoc14,kichThuoc12,kichThuoc11

soLuongTau = 12


def createMap(banDo):
    for i in range(0,Map["doc"]):
        arr = []
        for j in range(0,Map["ngang"]):
            arr.append(sign)
        banDo.append(arr)

    taoMotTau(banDo,kichThuoc27)
    taoMotTau(banDo,kichThuoc25)
    taoMotTau(banDo,kichThuoc25)
    taoMotTau(banDo,kichThuoc14)
    taoMotTau(banDo,kichThuoc14)
    taoMotTau(banDo,kichThuoc14)
    taoMotTau(banDo,kichThuoc12)
    taoMotTau(banDo,kichThuoc12)
    taoMotTau(banDo,kichThuoc12)
    taoMotTau(banDo,kichThuoc11)
    taoMotTau(banDo,kichThuoc11)
    taoMotTau(banDo,kichThuoc11)



# f = open("viTriTau.txt","w")
# for i in range(0,Map["doc"]):
#     for j in range(0,Map["ngang"]):
#         f.write(str(banDo[i][j])+"  ")
#     f.write("\n")





""" 
bản đồ
0 0 0 0 0 0 0 0 X 
0 0 0 0 0 0 0 0 X 
0 0 0 X X 0 0 0 0 
0 0 0 X X 0 0 0 0
0 0 0 0 0 0 0 0 0 

kích thước tàu : 
1. X             : 3 
2. X X           : 3 
3. X X X X       : 3 
4. X X X X X     : 2 
   X X X X X
5. X X X X X X X : 1
   X X X X X X X

2 kích thước : dai,rong 
2 chiều : ngang,doc


"""

