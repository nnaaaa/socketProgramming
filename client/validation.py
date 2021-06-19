import getpass

def validate(user):
    if not user["account"]:
        print("👿 Account can't be blank")
        return False
    user["password"] = getpass.getpass(prompt="password: ")
    if not user["password"]:
        print("😡 Password can't be blank")
        return False
    else:
        return True


