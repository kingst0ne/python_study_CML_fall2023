'''
4.	Имеются два списка состоящие из произвольных элементов.
Напишите функцию которая возвращает пересечение списков
(элементы которые встречаются в и там и там)
'''

def comb_list(list1, list2):
    '''
    функцию возвращает пересечение списков
    :param list1: list
    :param list2: list
    :return: list
    '''
    res = []
    for i in list1:
        if i in list2 and i not in res:
            res.append(i)

    return res#list(set(list1)&set(list2))

lst1 = [1,2,[4,3],'a', 2]
lst2 = [3,2,[4,3],'b', 2]

print(comb_list(lst1, lst2))