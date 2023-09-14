


class Student:

    profession = 'Developer'

    def __new__(cls, *args, **kwargs):
        print('new')
        return super().__new__(cls)

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age





    def check_profession(self):
        print(self.profession)

    @staticmethod
    def student_location():
        print('SPb')




new_student = Student('Ivan', 'Ivanov', 22)

print(new_student.last_name)
print(new_student.first_name)
print(new_student.age)
new_student.student_location()
# new_student.last_name()


pass
