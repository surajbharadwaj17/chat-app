########## Subscription DAO #########

from db.database import DBConfig, DBManager

class SubscriptionDAO:
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

    def get_subscription(self, id):
        return self.db.select(table='t_subscriptions', filters={'id':id})

    def create_subscription(self, data):
        if data:
            sql = self.db.insert(table='t_subscriptions', data=data)
            self.db.execute(sql)

    def update_subscription(self, id, data):
        if data:
            sql = self.db.update(table='t_subscriptions', filters={'id':id}, data=data)
            self.db.execute(sql)

    def delete_channel(self, id):
        pass


subs_dao = SubscriptionDAO()

sub = {
    'user' : 1,
    'channel' : 1,
    'status' : 'ACTIVE'
}

print(subs_dao.get_subscription(id=1))