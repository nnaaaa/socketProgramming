import ast
import time

def gameRoute(client,data,usersOnline):
    if (data["game"] == "start_game"):
        accounts = list(map(lambda user: user["account"],usersOnline))
        client["socket"].send(bytes(str(accounts),'utf8'))

    elif(data["game"] == "create_room"):
        userOnline = list(filter(lambda user: user["account"] == data["account"],usersOnline))
        userOnline[0]["socket"].send(bytes(str("play-game"),'utf8'))
        client["socket"].send(bytes(str("play-game"),'utf8'))
        # user này không online
        # if len(userOnline) != 0 :
        #     respond["err"] = "User doesn't online"
        #     client["socket"].send(bytes(str(respond),'utf8'))

        # gửi thông báo cho user kia
        # request = {
        #     "invitation":"create_room",
        #     "account":client["account"]
        # }
        #isAccept = ast.literal_eval(client["socket"].recv(1024).decode("utf8"))
        #print("accept:", isAccept)

    elif (data["game"] == "waiting"):
        IsLookingFor = list(filter(lambda user : user["account"] == client["account"],usersOnline))
        





        
        
