import numpy as np

# X = np.array([394 for x in range(20)])
# print(X)

# X = [1,2,5,20,25,100]
# X = [x*2 if x in range(1,21) else x for x in X ]
# print(X)



def fun(*args):
    res = sorted(list(filter(lambda elem: type(elem) is int, args)))
    if res == []:
        raise Exception()
    return res


print(fun(1,2, 'i', -8))
print(fun('1,2,' 'i'))

