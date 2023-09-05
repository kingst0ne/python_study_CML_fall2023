#
#
# double = lambda x:x*2
#
# print(double(5))
#
# list_val = [1,2,3,4,5,6,7,8,9,10]
#
# print(list(filter(lambda x:x%2 == 0, list_val)))
#
#
# str = 'pop abc tre'
#
# print(list(filter(lambda x:x!=' ', str)))
#
#
# str = ['pop abc tre',1,2, 3.0 ,'ooo',5.]
#
# print(list(filter(lambda x:type(x)==int, str)))
#
# numbers = [1,2,3,4,5,56]
#
# def filter_num(is_num):
#     return is_num%2 ==0
#
# print(list(filter(filter_num,numbers)))

#
# def square(num):
#     return num**2
#
# numbers = [1,2,3,4,5,56]
# print(list(map(square, numbers)))


# str = ['1', '2', '5', '6']
#
# print(list(map(int, str)))

# str2 = 'pop abc tre'
# print(list(map(str.upper, str2)))
#
# print(''.join(list(map(str.upper, str2))))

str = ['1', '2', '5333', '62']


print(list(map(len, str)))