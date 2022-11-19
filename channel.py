########## Channel DAO #########

from database import DBConfig, DBManager

class ChannelDAO:
    def __init__(self) -> None:
        self.db = DBManager(
            dbConfig=DBConfig(
                user="postgres",
                pwd="postgres",
                host="localhost",
                port="2345",
                name="chat",
                schema="chats"
            )
        )

    def get_channel(self, id):
        pass

    def create_channel(self, data):
        pass

    def update_channel(self, id, data):
        pass

    def delete_channel(self, id):
        pass


channel_dao = ChannelDAO()