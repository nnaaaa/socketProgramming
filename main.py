import validation
import authentication

user = {}
while True:
    commandline = input()
    chose = commandline.split(" ")[0]
    if not chose:
        continue
    if chose == "quit":
        break

    elif chose == "login":
        chose = commandline.split(" ")
        if len(chose) == 2:
            user["account"] = chose[1]
            if validation.validate(user):
                if authentication.auth(user):
                    encrypt = input("🤔 Do you want to encrypt message before sending? ")
                    if encrypt == "Y":
                        print("encrypt here")    # encrypt code
                    else:
                        print("no encrypt here")    # no encrypt code
                    # send user info to server here
                    print("💚 Login successfully")
        else:
            user["account"] = ""
            validation.validate(user)

    elif chose == "register":
        chose = commandline.split(" ")
        if len(chose) == 2:
            user["account"] = chose[1]
            if validation.validate(user):
                if authentication.signup(user):
                    encrypt = input("🤔 Do you want to encrypt message before sending? ")
                    if encrypt == "Y":
                        print("encrypt here")    # encrypt code

                    else:
                        print("no encrypt here")    # no encrypt code
                    # send user info to server here
                    print("🎄 Register successfully")  
        else:
            user["account"] = ""
            validation.validate(user)