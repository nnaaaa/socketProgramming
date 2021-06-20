import getpass
import socket
import numpy

from validation import validate,comparePassword
from api import signin,signup,changePassword,checkUser

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
                    print("encrypt here")    # encrypt ở đây
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
                    print("encrypt here")    # encrypt ở đây
                if signup(user,s):
                    print("🎄 Register successfully")  
        else:
            user["account"] = ""
            validate(user)

    elif chose.split("-")[0] == "check_user":
        # cắt khoảng trắng lấy được account
        chose = commandline.split(" ")
        if len(chose) < 2:
            continue
        chose[0] = chose[0].split("-")
        if len(chose[0]) == 2:
            option = chose[0][1]
            account = chose[1]
            checkUser(option,account,s)

    elif not login:
        continue
    
    elif chose == "change_password":
        if not login:
            print("You haven't signed in")
        if comparePassword(user["password"]):
            user["password"] = getpass.getpass(prompt="new password: ")
            encrypt = input("🤔 Do you want to encrypt message before sending? ")
            if encrypt == "Y":
                print("encrypt here")    # encrypt ở đây
            changePassword(user,s)
            print("🥊 Update password successfully")
    
    elif chose.split("-")[0] == "setup_info":
        # cắt khoảng trắng lấy được data
        chose = commandline.split(" ")
        if len(chose) < 2:
            continue
        chose[0] = chose[0].split("-")
        if len(chose[0]) == 2:
            option = chose[0][1]
            account = chose[1]
            # setInfo(option,account,s)

    



