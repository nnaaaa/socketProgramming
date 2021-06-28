from createShip import Map,taoMotTau,water,kichThuoc27,kichThuoc25,kichThuoc14,kichThuoc12,kichThuoc11

soLuongTau = 12

banDo = []
def createMap(banDo):
    for i in range(0,Map["doc"]):
        arr = []
        for j in range(0,Map["ngang"]):
            arr.append(water)
        banDo.append(arr)

    taoMotTau(banDo,kichThuoc27,"A")
    taoMotTau(banDo,kichThuoc25,"K")
    taoMotTau(banDo,kichThuoc25,"Q")
    taoMotTau(banDo,kichThuoc14,"J")
    taoMotTau(banDo,kichThuoc14,"9")
    taoMotTau(banDo,kichThuoc14,"8")
    taoMotTau(banDo,kichThuoc12,"7")
    taoMotTau(banDo,kichThuoc12,"6")
    taoMotTau(banDo,kichThuoc12,"5")
    taoMotTau(banDo,kichThuoc11,"4")
    taoMotTau(banDo,kichThuoc11,"3")
    taoMotTau(banDo,kichThuoc11,"2")


createMap(banDo)

f = open("client/game/viTriTau.txt","w")
for i in range(0,Map["doc"]):
    for j in range(0,Map["ngang"]):
        f.write(str(banDo[i][j])+"  ")
    f.write("\n")





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

