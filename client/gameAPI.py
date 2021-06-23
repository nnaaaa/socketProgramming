import ast
def getUsersOnline(socket):
    obj = {"game":"start_game"}
    socket.send(bytes(str(obj),'utf8'))
    listUsers = ast.literal_eval(socket.recv(1024).decode('utf8'))
    return listUsers

