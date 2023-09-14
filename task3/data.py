class Data:

    def __new__(cls, *args, **kwargs):
        print('state fetching')
        return super().__new__(cls)

    def __init__(self, lst):
        self.lst = lst
        print(f'data processing {self.lst}')


test1 = Data([1,2,3])

