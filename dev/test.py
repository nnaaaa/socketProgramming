import threading
import time
import sys
def minhduc(delay):
    while True:
        time.sleep(2)
        print("pass")
        yield 1

def quocthang(delay):
    func = minhduc(1)
    while True:
        y = input("nhap quocthang: ")


    
def room(DucThread,ThangThread):
    DucThread.start()
    # ThangThread.start()
    time.sleep(2)
    print("in room")

DucThread=threading.Thread(target=minhduc,args=(3,))
ThangThread=threading.Thread(target=quocthang,args=(4,))
RoomThread=threading.Thread(target=room,args=(DucThread,ThangThread))

if __name__ == "__main__":
   print("in main")
   RoomThread.start()
   m = minhduc(1)
   while True:
       time.sleep(2)
       print("1:",m.__next__())

