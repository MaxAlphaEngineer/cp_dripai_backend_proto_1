import socket

HEADER = 64
PORT = 3000
FORMAT = 'utf-8'
DISCONNECT_MASSAGE = "!DISCONNECT"
SERVER = '127.0.0.1'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    massage = msg.encode(FORMAT)
    msg_length = len(massage)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(massage)
    print(client.recv(2048).decode(FORMAT))


send("hello world !")
input()
send(DISCONNECT_MASSAGE)