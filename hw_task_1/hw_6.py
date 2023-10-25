'''
6)	Функция на вход получает список,
состоящий из 5 произвольных чисел.
Найти количество положительных чисел среди них.
'''

def amount_of_pos(lst):
    '''

    :param lst:
    :return:
    '''
    count = 0
    for num in lst:
        if num > 0:
            count +=1
    return count

lst1 = [1,0,-1,5,0,-7]

print(amount_of_pos(lst1))
