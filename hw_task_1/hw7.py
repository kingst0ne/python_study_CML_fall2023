'''
Функция на вход получает 2 переменные.
a)	Кол-во лет (int)
b)	Кол-во месяцев (int)
Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.

'''

def amount_of_days(years, month):
    '''

    :param years:
    :param month:
    :return:
    '''

    return (years*12 + month)*29

print(amount_of_days(2,4))