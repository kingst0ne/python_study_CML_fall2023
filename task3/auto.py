

class Car:
    def __init__(self, brand, model, year_of_prod, price):
        self.brand = brand
        self.model = model
        self.year_of_prod = year_of_prod
        self.price = price


class Passanger_car(Car):
    def __init__(self, num_doors, type, brand, model, year_of_prod, price):
        self.num_doors = num_doors
        self.type = type
        super().__init__(brand, model, year_of_prod, price)
    def __str__(self):
        return f'{self.num_doors, self.type, self.brand, self.model, self.year_of_prod, self.price}'


car1 = Passanger_car(4, 'crossover', 'toyota', 'rav4', 2021, 4000000)

print(car1)