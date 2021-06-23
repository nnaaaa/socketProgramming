def gameRoute(client,data,usersOnline,account):
    if (data["game"] == "start_game"):
        client.send(bytes(str(usersOnline),'utf8'))
