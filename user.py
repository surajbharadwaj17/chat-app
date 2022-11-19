###### User DAO #######
from database import DBConfig, DBManager

class UserDAO:
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

    def _validate_user_data(self, data):
        for key in ("name", "email"):
            if key not in data:
                return False
        return True

    def get_user(self, id):
        return self.db.select(table='t_users', 
                        filters={'id':id})


    def create_user(self, data):
        if self._validate_user_data(data):
            sql = self.db.insert(table='t_users', data=data)
            self.db.execute(sql)

    def update_user(self, id, data):
        pass

    def delete_user(self, id):
        pass


user_dao = UserDAO()

user = {
    'name' : 'Sooraj Bharadwaj',
    'email' : 'soorajbh@buffalo.edu'
}

#user_dao.create_user(data=user)
print(user_dao.get_user(id=1))