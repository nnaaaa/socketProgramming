import getpass
import socket

from validation import validate,comparePassword
from api import signin,signup,changePassword

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

user = {}
login = False
connect = False

while True:
    commandline = input()
    chose = commandline.split(" ")[0]
    if not chose:
        continue
    if chose == "quit":
        break
    elif chose == "connect":
        array = commandline.split(" ")
        if len(array)<4:
            print("🥵 Connection failed")
            continue
        ip = array[1]
        port = array[3]
        s.connect((socket.gethostname(),int(port)))
        connect = True
    elif not connect:
        continue

    elif chose == "login":
        chose = commandline.split(" ")
        if len(chose) == 2:
            user["account"] = chose[1]
            if validate(user):      
                encrypt = input("🤔 Do you want to encrypt message before sending? ")
                if encrypt == "Y":
                    print("encrypt here")    # encrypt code
                else:
                    print("no encrypt here")    # no encrypt code
                if signin(user,s):
                    print("💚 Login successfully")
                login = True
        else:
            user["account"] = ""
            validate(user)

    elif chose == "register":
        chose = commandline.split(" ")
        if len(chose) == 2:
            user["account"] = chose[1]
            if validate(user):
                encrypt = input("🤔 Do you want to encrypt message before sending? ")
                if encrypt == "Y":
                    print("encrypt here")    # encrypt code

                else:
                    print("no encrypt here")    # no encrypt code
                if signup(user,s):
                    print("🎄 Register successfully")  
        else:
            user["account"] = ""
            validate(user)
    
    elif chose == "change_password":
        if not login:
            print("You haven't signed in")
        if comparePassword(user["password"]):
            user["password"] = getpass.getpass(prompt="new password: ")
            encrypt = input("🤔 Do you want to encrypt message before sending? ")
            if encrypt == "Y":
                print("encrypt here")    # encrypt code
            else:
                print("no encrypt here")    # no encrypt code
            changePassword(user,s)
            print("🥊 Update password successfully")


