import socket
import ast

def playerAttack(socket,account):
    playing = True 
    blankMap = ast.literal_eval(socket.recv(4096).decode('utf8'))
    while playing:
        print("Enemy Map ----------------------------------------")
        displayMap(blankMap)
        commandline = input("🎮 This is your turn ")
        chose = commandline.split(" ")
        y = chose[1]
        x = chose[2]
        obj = {
            "attack":True,
            "position":{"x":int(x),"y":int(y)}     
        }
        socket.send(bytes(str(obj),'utf8'))
        blankMap = ast.literal_eval(socket.recv(4096).decode('utf8'))
        print(f"⛳ Waiting for {account}'s attack")
        
        updatedMap = ast.literal_eval(socket.recv(4096).decode('utf8'))

        print(f"Your Map -----------------------------------------")
        displayMap(updatedMap)



def playerDefend(socket,account):
    playing = True 
    blankMap = ast.literal_eval(socket.recv(4096).decode('utf8'))
    while playing:
        print(f"⛳ Waiting for {account}'s attack")
        updatedMap = ast.literal_eval(socket.recv(4096).decode('utf8'))
        print("Your Map -----------------------------------------")
        displayMap(updatedMap)
        print("Enemy Map ----------------------------------------")
        displayMap(blankMap)
        commandline = input("🎮 This is your turn ")
        chose = commandline.split(" ")
        y = chose[1]
        x = chose[2]
        obj = {
            "attack":True,
            "position":{"x":int(x),"y":int(y)} 
        }
        socket.send(bytes(str(obj),'utf8'))
        blankMap = ast.literal_eval(socket.recv(4096).decode('utf8'))
        

def displayMap(mmap):
    for i in mmap:
        print(i)

        
