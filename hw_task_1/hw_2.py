'''
Напишите функцию которая
a)	принимает два списка
b)	возвращает длину самого длинного
'''

def two_lists_check(list1, list2):
    '''
    Функция принимает два списка, возвращает длину самого длинного
    :param list1: список 1. формат list
    :param list2:список 2. формат list
    :return: длина наибольшего
    '''
    if type(list1) and type(list2) != list:
        raise TypeError('Тип несоответствует списку')
    if len(list1) > len(list2):
        return len(list1)
    return len(list2)


list1 = [1,2,3]
list2 = [1,2,3,4]
print(two_lists_check(list1,list2))

list1 = [1,2,3,4,5]
list2 = [1,2,3,[4,5]]
print(two_lists_check(list1,list2))

list1 = 'test'
list2 = 'test2'
print(two_lists_check(list1,list2))