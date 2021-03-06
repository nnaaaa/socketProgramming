from encrypt import decrypt
import pymongo
db = pymongo.MongoClient('mongodb+srv://cusa789:123tumodi@cluster0.z53no.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
collection = db["Facebook"]
users = collection.users

def postLogin(userParams):
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
    if userParams["isEncrypt"] == True:
        userParams["password"] = decrypt(userParams["password"])
    if userParams["password"] != user["password"]:
        err["password"] = True
        return err
    return err

def postRegister(userParams):
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
        #xóa lệnh ra khỏi user 
        userParams.pop("auth")
        if userParams["isEncrypt"] == True:
            userParams["password"] = decrypt(userParams["password"])
        userParams.pop("isEncrypt")
        #khởi tạo điểm
        userParams["point"] = 0
        #thêm tài khoản vào database
        users.insert_one(userParams)
        return err

def getUser(userParams):
    user = users.find_one({"account":userParams["account"]})
    # gỡ id trước khi gửi về client để tránh bị lỗi khi dùng ast 
    if user:
        user.pop("_id")
        user["exist"] = True
        return user
    else:
        user = {
            "exist":False
        }
        return user

def updateUser(userParams):
    #xóa lệnh ra khỏi user 
    userParams.pop("auth")
    if 'isEncrypt' in userParams.keys():
        if userParams["isEncrypt"] == True:
            userParams["password"] = decrypt(userParams["password"])
        userParams.pop("isEncrypt")
    # update thông tin lên database
    users.update_one({"account":userParams["account"]},{"$set":userParams})

def updatePoint(userParams):
    user = users.find_one({"account":userParams["account"]})
    user["point"] += userParams["point"]
    users.update_one({"account":userParams["account"]},{"$set":user})

