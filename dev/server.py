import socket
import sys
import traceback
from threading import Thread


def main():
    start_server()

def start_server():
    host = "127.0.0.1"
    port = 8000  # arbitrary non-privileged port
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    soc.bind((host, port))
    while True:
        connection, address = soc.accept()
        ip, port = str(address[0]), str(address[1])
        Thread(target=clientThread, args=(connection, ip, port)).start()
        """ def Thread():
            -nhận dữ liệu connection.recv
            -dữ liệu là tạo phòng -> Thread(target=clientThread, args=(connection, ip, port)).start()
            -gửi qua 2 luồng kia join vào thread này
            -gửi thông báo đã join về client "join" -> gửi bản đồ lên server 

            server: nhận được 2 bản đồ -> client_1 attack -> client_2 -> ...... -> kết thúc
        """    
    soc.close()












def clientThread(connection, ip, port, max_buffer_size=5120):
    is_active = True
    while is_active:
        client_input = receive_input(connection, max_buffer_size)
        if "--QUIT--" in client_input:
            print("Client is requesting to quit")
            connection.close()
            print("Connection " + ip + ":" + port + " closed")
            is_active = False
        else:
            print("Processed result: {}".format(client_input))
            connection.sendall("-".encode("utf8"))


def receive_input(connection, max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)
    if client_input_size > max_buffer_size:
        print("The input size is greater than expected {}".format(client_input_size))
    decoded_input = client_input.decode("utf8").rstrip()
    result = process_input(decoded_input)
    return result


def process_input(input_str):
    print("Processing the input received from client")
    return "Hello " + str(input_str).upper()


if __name__ == "__main__":
    main()
