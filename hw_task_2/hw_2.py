'''
Имеется список, состоящий из чисел.
Напишите функцию которая принимает число и возвращает
список состоящий из элементов первого списка кратных входному параметру.
'''

def div_check(lst, num):
    '''
    Функция возвращает список состоящий из элементов
    первого списка кратных входному параметру
    :param lst: List, list
    :param num: число, int
    :return: list
    '''
    lst2 = []
    for number in lst:
        if number%num == 0:
            lst2.append(number)
    return lst2

lst1 = [1,2,3,4,5,6]

print(div_check(lst1,3))