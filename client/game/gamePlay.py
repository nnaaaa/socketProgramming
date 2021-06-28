import socket
import ast

def playerAttack(socket):
    playing = True 
    while playing:
        commandline = input("Input attack position:")
        chose = commandline.split(" ")
        x = chose[1]
        y = chose[2]
        obj = {
            "game":"attack",
            "position":{"x":x,"y":y}
            
        }

        socket.send(bytes(str(obj),'utf8'))



def playerDefend(socket):
    playing = True 
    while playing:
        print("Waiting for opponent's attack:")
        attackPosition = ast.literal_eval(socket.recv(4096).decode('utf8'))
        
