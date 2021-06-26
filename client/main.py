
import ast
import stdiomask
import re
import socket

from validation import validate,comparePassword
from userAPI import signin,signup,changePassword,checkUser,setInfo
from gameAPI import getUsersOnline,inviteToPlay
from middlewares import receiveData

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
        port = array[3]
        try:
            s.connect((socket.gethostname(),8000))
            connect = True
        except:
            connect = False
        #threading.Thread(target=receiveData,args=(s,False)).start()

    elif not connect:
        continue

    elif chose == "close" or chose == "end":    
        s.close()
        break

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
        chose = commandline.replace("-"," ").split(" ")
        if len(chose) < 3:
            print("🥵 Fail command line")
            continue
        option = chose[1]
        account = chose[2]
        checkUser(option,account,s)

    elif not login:
        continue

    #game--------------------------------------------------------------------------------
    elif chose == "waiting":
        data = s.recv(1024).decode('utf8')
        if 'play-game' in data:
            chose = input(f"Do you want to play [Y/N] ")
            if chose == "Y":
                s.send(bytes(str({"concho":"conchoNguyenThang"}),'utf8'))
                print("Start game!!!!!!")
            elif chose == "N":
                s.send(bytes(str({"concho":"conchoNguyenThang"}),'utf8'))
            else:
                print("Cut")

    elif chose == "start_game":
        usersOnline = getUsersOnline(s)
        print("[Server] List users online:")
        for user in usersOnline:
            print(f"✅ {user}")
    
    elif chose == "create_room":
        chose = commandline.split(" ")
        option = chose[0]
        room = chose[1]
        account = chose[3]
        respond = inviteToPlay(option,room,account,s)

    elif chose ==    :
        #do nothing
        
    #game--------------------------------------------------------------------------------
    
    elif chose == "change_password":
        if not login:
            print("You haven't signed in")
        if comparePassword(user["password"]):
            user["password"] = stdiomask.getpass("new password: ")
            encrypt = input("🤔 Do you want to encrypt message before sending? ")
            if encrypt == "Y":
                print("encrypt here")    # encrypt ở đây
            changePassword(user,s)
            print("🥊 Update password successfully")
    
    elif chose.split("-")[0] == "setup_info":
        # cắt khoảng trắng lấy được data
        chose = commandline.replace("-"," ")
        chose = re.split(" ",chose,2)
        if len(chose) < 3:
            print("🥵 Fail command line")
            continue
        option = chose[1]
        string = chose[2]
        account = user["account"]
        setInfo(option,string,account,s)

    print("-"*50)

    



