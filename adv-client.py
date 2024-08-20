import socket

HEADER = 64
PORT = 8021
FORMAT = 'utf-8'
DISCONNECT_MSG = "DISCONNECT"
SERVER = "192.168.96.203"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def receive():
    try:
        length_msg = client.recv(HEADER).decode(FORMAT)
        if length_msg:
            length_msg = int(length_msg)
            message = client.recv(length_msg).decode(FORMAT)
            print(f"Server: {message}")
    except Exception as e:
        print(f"Error: {e}")

# วงจรการสื่อสารต่อเนื่อง
connected = True
while connected:
    msg = input(" TOP => ")
    send(msg)
    if msg == DISCONNECT_MSG:
        connected = False
    else:
        receive()

client.close()
