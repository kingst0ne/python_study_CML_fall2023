'''
1)	Напишите функцию которая возвращает длину принимаемой строки,
по умолчанию строка пустая (s=’’).
Пропишите все аннотации.
'''

def length_str_determination(s=''):
    '''
    Функция озвращает длину принимаемой строки, по умолчанию строка пустая
    :param s: строка на вход
    :return: длину строки
    '''
    return len(s)


print(length_str_determination())
print(length_str_determination('test2'))