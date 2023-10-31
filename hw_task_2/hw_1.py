'''
Имеется строка состоящая из слов.
Напишите функцию которая возвращает строку убрав из нее стоп слова.
Стоп слова находятся в списке:

[“Python”, “php”, “go”, “C”]

'''

def stop_sign(str1):
    '''
    Функцию возвращает строку убрав из нее стоп слова
    :param str1: строка, str
    :return: строка, str
    '''
    stop_words = ['Python', 'php', 'go' ,'C']
    new_str = ''
    for word in str1.split():
        if word in stop_words:
            pass
        else:
            new_str+=word+' '

    return new_str.strip()

str1 = 'Python мой любимый язык программирования'
str2 = 'я люблю php '

print(stop_sign(str1))
print(stop_sign(str2))