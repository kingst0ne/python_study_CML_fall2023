
# def currency(fn):
#     def wrapper(*args, **kwargs):
#         result = fn(*args, **kwargs)
#         return f'{result} руб'
#     return wrapper
#
# @currency
# def price_calc(price, tax):
#     return price*(1+tax)
#
#
#
# print(price_calc(100,0.05))

def results(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f'Результат вычислений: {result}'
    return wrapper

@results
def square(num):
    return num**2

@results
def multipl(num):
    return num*2


print(square(100))
print(multipl(100))



