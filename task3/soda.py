

class Soda:
    def __init__(self, addition_type = None):
        self.addition_type = addition_type

    def show_my_drink(self):
        if self.addition_type:
            print('Обычная газировка')
        else:
            print(f'Газировка и {self.addition_type}')


soda1 = Soda()

soda2 = Soda('Лимон')

soda1.show_my_drink()
soda2.show_my_drink()