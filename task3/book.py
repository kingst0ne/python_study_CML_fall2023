

class Book:
    def __init__(self, title, author, checked_out = False):
        self.title = title
        self.author = author
        self.check = checked_out

    def check_out(self):
        if not self.check:
            print('Выдаем книгу абонету')
            self.check = True
        else:
            print('Книга у абонента')

    def check_in(self):
        if self.check:
            print('Принимаем книгу у абонента')
            self.check = False
        else:
            print('Книга в наличии')




book1 = Book('Преступление и наказание', 'Достоевский')

book1.check_out()
book1.check_out()
book1.check_in()
book1.check_in()

