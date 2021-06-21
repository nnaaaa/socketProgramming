from createShip import taoMotTau,sign

banDo = []
soLuongTau = 12

for i in range(0,20):
    arr = []
    for j in range(0,20):
        arr.append(sign)
    banDo.append(arr)


taoMotTau(banDo,{"dai":7,"rong":2})

taoMotTau(banDo,{"dai":5,"rong":2})
taoMotTau(banDo,{"dai":5,"rong":2})

taoMotTau(banDo,{"dai":4,"rong":1})
taoMotTau(banDo,{"dai":4,"rong":1})
taoMotTau(banDo,{"dai":4,"rong":1})

taoMotTau(banDo,{"dai":2,"rong":1})
taoMotTau(banDo,{"dai":2,"rong":1})
taoMotTau(banDo,{"dai":2,"rong":1})

taoMotTau(banDo,{"dai":1,"rong":1})
taoMotTau(banDo,{"dai":1,"rong":1})
taoMotTau(banDo,{"dai":1,"rong":1})

f = open("viTriTau.txt","w")
for i in range(0,20):
    for j in range(0,20):
        f.write(str(banDo[i][j])+" ")
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


1 . góc trên bên trái : X >= 0 , Y >= 0
2 . góc trên bên phải :(ngang) X + dai <= 19 ,  y >= 0     
                        (doc) X + rong <= 19 , y >= 0 
3 . góc dưới bên trái :(ngang) X >= 0 , Y + rong <= 19
                        (doc) X >= 0 , y + dai <= 19
4 . góc dưới bên phải :(ngang) X + dai <= 19 , Y + rong <= 19
                        (doc) X + rong <= 19 , Y + dai <= 19

"""

