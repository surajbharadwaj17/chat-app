import socket

HOST = "127.0.0.1"
PORT = 60356

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    while True:
        con, addr = sock.accept()
        with con:
            print(f"Connected by {addr}")
            while True:
                data = con.recv(1024)
                if not data:
                    break
                con.sendall(data)