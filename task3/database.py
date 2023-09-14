

class DataBase:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print(f'connect to DB {self.user}, {self.password}, {self.port}')

    @staticmethod
    def close():
        print('close connection with DB')


conn1 = DataBase('aaa', 'bbbb', 1212)

conn2 = DataBase('aaa', 'wwww', 1212)

conn1.connect()
conn2.connect()
