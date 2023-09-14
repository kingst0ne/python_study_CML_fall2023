
class Salary:

    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return self.pay*12

class Employee:

    def __init__(self, pay, bonus):

        self.salary = Salary(pay)
        self.bonus = bonus

    def annual_pay(self):
        return f'Total: {self.salary.get_total() + self.bonus}'


obj1 = Employee(25000, 10000)

print(obj1.annual_pay())