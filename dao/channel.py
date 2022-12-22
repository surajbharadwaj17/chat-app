########## Channel DAO #########

from db.database import DBConfig, DBManager

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
        return self.db.select(table='t_channels', filters={'id':id})

    def create_channel(self, data):
        if data:
            sql = self.db.insert(table='t_channels', data=data)
            self.db.execute(sql)

    def update_channel(self, id, data):
        if data:
            sql = self.db.update(table='t_channels', filters={'id':id}, data=data)
            self.db.execute(sql)

    def delete_channel(self, id):
        pass



# channel_dao = ChannelDAO()

# channel = {
#     'name' : 'Test',
#     'description' : 'test',
#     'admin' : 1
# }

# channel2 = {
#     'name' : 'Test_update',
#     'description' : 'test_update',
#     'admin' : 1
# }

# #channel_dao.create_channel(data=channel)
# channel_dao.update_channel(id=1, data=channel)
# print(channel_dao.get_channel(id=1))
