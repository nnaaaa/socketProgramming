import pymongo
client = pymongo.MongoClient('mongodb+srv://cusa789:123tumodi@cluster0.z53no.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client["Facebook"]

def postLogin(userParams):
    users = db.users
    #tìm tài khoản trong database
    user = users.find_one({"account":userParams["account"]})
    err = {
        "account": False,
        "password": False
    }
    # tài khoảng không tồn tại
    if not user:
        err["account"] = True
        return err
    # mật khẩu không khớp
    if userParams["password"] != user["password"]:
        err["password"] = True
        return err 
    return err

def postRegister(userParams):
    users = db.users
    #tìm tài khoản trong database
    user = users.find_one({"account":userParams["account"]})
    err = {
        "account": False,
    }
    # tài khoản tồn tại
    if user:
        err["account"] = True
        return err
    else:
        #thêm tài khoản vào database
        users.insert_one(userParams)
        return err