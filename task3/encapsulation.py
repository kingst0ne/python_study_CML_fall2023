class Encapsulation:

    def __init__(self):
        self.open_param = {'db_name':'student', 'db_port' : 123}
        self.__config = {'db_user' : 'root', 'db_pass': '111'}


obj = Encapsulation()

print(obj.open_param)

# print(obj.__class__().__config)
