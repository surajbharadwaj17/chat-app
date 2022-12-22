from socket_server import SocketConfig, SocketServer


class SocketServerManager:
    def __init__(self, data) -> None:
        self.data = data

    def create_server(self):
        """Return SocketServer object"""
        return SocketServer(host=self.data["host"], port=self.data["port"])

    
    