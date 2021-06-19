import pymongo
client = pymongo.MongoClient('mongodb+srv://cusa789:123tumodi@cluster0.z53no.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client["Facebook"]

def postLogin(userParams):
    users = db.users
    user = users.find_one({"account":userParams["account"]})
    err = {
        "account": False,
        "password": False
    }
    if not user:
        err["account"] = True
        return err
    if userParams["password"] != user["password"]:
        err["password"] = True
        return err 
    return err

def postRegister(userParams):
    users = db.users
    user = users.find_one({"account":userParams["account"]})
    err = {
        "account": False,
    }
    if user:
        err["account"] = True
        return err
    else:
        users.insert_one(userParams)
        return err