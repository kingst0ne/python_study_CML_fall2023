'''
5)	Напишите функцию которая отвечает “ДА” или “НЕТ” на вопрос в комментарие

str_2 содержит в себе str_1?
'''

def str_in_str(str1, str2):
    if str1 in str2:
        print('ДА')
    else:
        print('НЕТ')

str1 = 'test'
str2 = 'test1'

str_in_str(str1,str2)

str1 = 'test'
str2 = 'tes1'

str_in_str(str1,str2)