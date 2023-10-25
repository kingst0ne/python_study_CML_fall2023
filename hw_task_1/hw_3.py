'''
Напишите функцию которая:
a)	принимает список с произвольными значениями
b)	добавляет к нему произвольное значение
c)	возвращает результирующий список

'''

def list_append(lst, a):
    '''

    :param lst:
    :param a:
    :return:
    '''
    lst1 = lst.append(a)

    return lst1

lst = [1,2,3]
a = 4


print(list_append(lst, a))