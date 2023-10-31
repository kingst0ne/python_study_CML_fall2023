'''
3.	Напишите функцию, которая принимает любое количество
не именованных аргументов и возвращает кортеж состоящий
из аргументов у которых тип данных str
'''

def finding_str(*args):
    tpl = ()
    for elem in args:
        if type(elem) == str:
            tpl += (elem,)
    return tpl

test = (1,'test', 2, True, 'good')

print(finding_str(1,'test', 2, True, 'good'))
