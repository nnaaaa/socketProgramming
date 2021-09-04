import stdiomask

def validate(user):
    if not user["account"]:
        print("👿 Account can't be blank")
        return False
    user["password"] = stdiomask.getpass("password: ")
    if not user["password"]:
        print("😡 Password can't be blank")
        return False
    else:
        return True

def comparePassword(user,decrypt):
    if user["isEncrypt"] == True:
        user["password"] = decrypt(user["password"])
    oldPassword = stdiomask.getpass("password: ")
    if oldPassword != user["password"]:
        print("Wrong password")
        return False
    else:
        return True





