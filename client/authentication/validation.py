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

def comparePassword(password):
    oldPassword = stdiomask.getpass("password: ")
    if oldPassword != password:
        print("Wrong password")
        return False
    else:
        return True





