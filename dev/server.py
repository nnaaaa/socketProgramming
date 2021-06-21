import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),8000))
s.listen(5)

while True:
    client,addr = s.accept()
    print(f"Client from {addr} connect")
    try:
        while True:
            msg = client.recv(1024)
            # nhận map bắn tàu trả về client khác 
            if not msg:
                print("client disconect")
                client.close()
                break

            msg = msg.decode("utf8")
            print('Client: ',msg)
            data = input('Server: ')
            client.send(bytes(data,'utf8'))

    finally:
        print("end")
s.close()

