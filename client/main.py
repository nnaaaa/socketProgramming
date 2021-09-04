import ast
import stdiomask
import re
import socket

from authentication.validation import validate,comparePassword
from api.userAPI import signin,signup,changePassword,checkUser,setInfo
from api.gameAPI import getUsersOnline,waiting,createRoom
from authentication.encode import encrypt, decrypt

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
            print("🥵 Fail command line")
            continue
        ip = array[1]
        port = int(array[3])
        try:
            s.connect((ip,port))
            connect = True
        except:
            print("fail to connect")
            connect = False

    elif not connect:
        continue


    elif chose == "close" or chose == "end":
        s.close()
        break

    elif chose == "login" and not login:
        chose = commandline.split(" ")
        if len(chose) == 2:
            user["account"] = chose[1]
            if validate(user):
                user["isEncrypt"] = False
                isEncrypt = input("🤔 Do you want to encrypt message before sending? ")
                if isEncrypt == "Y":
                    user["password"] = encrypt(user["password"])    # encrypt ở đây
                    user["isEncrypt"] = True
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
                user["isEncrypt"] = False
                isEncrypt = input("🤔 Do you want to encrypt message before sending? ")
                if isEncrypt == "Y":
                    user["password"] = encrypt(user["password"])    # encrypt ở đây
                    user["isEncrypt"] = True
                if signup(user,s):
                    print("🎄 Register successfully")  
        else:
            user["account"] = ""
            validate(user)

    elif chose.split("-")[0] == "check_user":
        chose = commandline.replace("-"," ").split(" ")
        if len(chose) < 3:
            print("🥵 Fail command line")
            continue
        checkUser(chose[1],chose[2],s)

    elif not login:
        continue

    #game--------------------------------------------------------------------------------
    elif chose == "waiting":
        waiting(s)

    elif chose == "start_game":
        usersOnline = getUsersOnline(s)
        print("[Server] List users online:")
        for user in usersOnline:
            print(f"✅ {user}")
    
    elif chose == "create_room":
        chose = commandline.split(" ")
        if len(chose) < 3:
            print("🥵 Fail command line")
            continue
        createRoom(chose[0],chose[1],chose[3],s)

    #game--------------------------------------------------------------------------------
    
    elif chose == "change_password":
        if not login:
            print("You haven't signed in")
        if comparePassword(user,decrypt):
            user["password"] = stdiomask.getpass("new password: ")
            isEncrypt = input("🤔 Do you want to encrypt message before sending? ")
            if isEncrypt == "Y":
                user["password"] = encrypt(user["password"])    # encrypt ở đây
                user["isEncrypt"] = True
            changePassword(user,s)
            print("🥊 Update password successfully")
    
    elif chose.split("-")[0] == "setup_info":
        # cắt khoảng trắng lấy được data
        chose = commandline.replace("-"," ")
        chose = re.split(" ",chose,2)
        if len(chose) < 3:
            print("🥵 Fail command line")
            continue
        setInfo(chose[1],chose[2],user["account"],s)

    print("-"*50)

