import pandas as pd
#
# ser = pd.Series([2,4,6,8,10])
#
# print(ser)
# print(ser[1])
# print(ser[:1])
#
#
#
# ser = pd.Series({2:'1',4:'2',6:'1',8:'1',10:'2'})
#
# print(ser)
# print(ser[2,1])
# print(ser[1])
#
# print(ser.values)
# print(ser.name)
# print(ser.size)
# print(ser.index)
#
#
# ser = pd.Series([2,4,6,8,10])
#
# print(ser >= 3)

# def ser_from_matrix(lst1, lst2):
#     try:
#         ser = pd.Series(lst1,index=lst2)
#         return ser
#     except:
#         pass
#
#
# lst1 = [1,2,3]
# lst2 = [3,4,5]
#
# ser = ser_from_matrix(lst1,lst2)
# print(ser)


dct = {'day1': 100, 'day2':0, 'day3': 300, 'day4':500}

ser = pd.Series(dct.pop('day4'))


print(ser[ser>0])

