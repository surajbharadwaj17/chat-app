import socket
from cache.redis_dao import RedisConfig, RedisManager
from dataclasses import dataclass

@dataclass
class SocketConfig:
    host: str
    port: int


HOST = "127.0.0.1"
PORT = 60356

class SocketServer:
    def __init__(self) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _bind(self, conf:SocketConfig):
        self.sock.bind((conf.host, conf.port))

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


