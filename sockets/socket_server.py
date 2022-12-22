import socket
#from cache.redis_dao import RedisConfig, RedisManager
from dataclasses import dataclass
from threading import Thread
from datetime import datetime

@dataclass
class SocketConfig:
    host: str
    port: int


HOST = "127.0.0.1"
PORT = 60356

class SocketServer:
    def __init__(self, host:str, port:int) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock_config = SocketConfig(host=host, port=port)
        self.connected = set()

    def _bind(self, conf:SocketConfig):
        self.sock.bind((conf.host, conf.port))

    def _listen(self):
        self.sock.listen()

    def _close(self):
        for addr,con in self.connected:
            con.close()

    def _listen_for_client(self, sock, addr):
        with sock:
            print(f"Connected by {addr}")
            while(True):
                try:
                    data = sock.recv(1024)
                    if not data:
                        break
                    
                    to_send = f"{addr}@{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} >> {data}"

                    for con, client_sock in self.connected:
                        if client_sock != sock:
                            client_sock.send(to_send.encode())
                except Exception as e:
                    print(f"Error: {e}")
                    self.connected.remove((addr, sock))


    def _start(self):
        self._bind(conf=self.sock_config)
        self._listen()

        while(True):
            client_sock, client_addr = self.sock.accept()
            self.connected.add((client_addr, client_sock))
            thread = Thread(target=self._listen_for_client, args=(client_sock, client_addr,))
            thread.daemon = True
            thread.start()
            # self._close()

    def run(self):
        self._start()

server = SocketServer(host="127.0.0.1", port=60356)
server.run()


