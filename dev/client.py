import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),8000))

print(socket.gethostname())

try:
    while True:
        msg = input('Client: ')
        if msg == "quit":
            s.close()
            break

        s.send(bytes(msg,'utf8'))
        data = s.recv(1024)
        print('Server: ',data.decode('utf8'))

finally:
    print("close")
