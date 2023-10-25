'''
9)	Напишите функцию для нахождения факториала числа.
'''

def factorial(n):
    '''
    Функцию для нахождения факториала числа
    :param n: число
    :return: факториал числа
    '''
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact

print(factorial(5))