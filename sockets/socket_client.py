import socket
import json
#from cache.redis_dao import RedisConfig, RedisManager
from dataclasses import dataclass
from threading import Thread
from datetime import datetime

@dataclass
class SocketConfig:
    host: str
    port: int

class SocketClient:

    def __init__(self, host, port, name) -> None:
        self.sock_config = SocketConfig(host=host, port=port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name = name
    
    def _connect(self):
        try:
            print(f"Connecting to {self.sock_config.host}:{self.sock_config.port}")
            self.sock.connect((self.sock_config.host, self.sock_config.port))
            print(f"Connected!")
        except Exception as e:
            print(f"Error: {e}")

    def _listen(self):
        while True:
            data = self.sock.recv(1024)
            print(f"Received data {data.decode()}")

    def _start(self):
        self._connect()
        thread = Thread(target=self._listen)
        thread.daemon = True
        thread.start()
        #self._chat()

    def _serialize(self, data):
        """Given a json, return the serialized byte object"""
        to_send = json.dumps(data).encode('utf-8')
        return to_send

    def _deserialize(self, data):
        """Given a serialized byte object, return deserialized json object"""
        to_recv = json.loads(data.decode('utf-8'))
        return to_recv

    def send_msg(self, msg):
        to_send = self._serialize(data={
            "name":  self.name,
            "data" : msg,
            "created_at" : datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        self.sock.send(to_send)
    
    def _chat(self):
        while True:
            user_input = input(">>")
            if user_input.lower() == '!q':
                break

            to_send = self._serialize(data={
                "name" : self.name,
                "data" : user_input,
                "created_at" : datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            self.sock.send(to_send)

    def run(self):
        self._start()

#client = SocketClient(host="127.0.0.1", port=60356, name="x")
#client.run()

