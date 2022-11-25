import socket

HOST = "127.0.0.1"
PORT = 60356

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(b'Hello boys!')
    data = sock.recv(1024)

print(f"Received data {data}")