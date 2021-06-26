import ast
def getUsersOnline(socket):
    obj = {"game":"start_game"}
    socket.send(bytes(str(obj),'utf8'))
    listUsers = ast.literal_eval(socket.recv(1024).decode('utf8'))
    return listUsers

def inviteToPlay(option,room,account,socket):
    obj={
        "game":option,
        "room":room,
        "account":account
    }
    socket.send(bytes(str(obj),'utf8'))
    respond = socket.recv(1024).decode('utf8')
    print("start game!!!")
    return respond
