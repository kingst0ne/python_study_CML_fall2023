class Collection:

    def __init__(self, lst):
        self.lst = lst

    def __len__(self):
        return len(self.lst)

    def __del__(self):
        print('delete')

obj1 = Collection([1,2,3])

print(len(obj1))

del obj1

#print(obj1)
