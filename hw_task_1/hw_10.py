'''
Замените классическое представление цикла for в примере на любую конструкцию
так чтоб результат оставался тот же.


'''

lst = [2,4,5,8,9,13]

res = list(map(lambda x, y: x * y, range(len(lst)), lst))
res2 = [x*lst[x] for x in range(len(lst))]

print(res2)
print(res)