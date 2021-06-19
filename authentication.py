import pymongo
client = pymongo.MongoClient('mongodb+srv://cusa789:123tumodi@cluster0.z53no.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client["Facebook"]

def auth(userParams):
    users = db.users
    user = users.find_one({"account":userParams["account"]})
    if not user:
        print("😩 Account doesn't exist")
        return False
    if userParams["password"] != user["password"]:
        print("😓 Wrong password")
        return False
    else:  
        return True

def signup(userParams):
    users = db.users
    user = users.find_one({"account":userParams["account"]})
    if user:
        print("😛 Account does exist")
        return False
    else:
        users.insert_one(userParams)
        return True