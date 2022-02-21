class SchoolMember:
    '''Представляет любого человека в школе'''
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        print('(Создан Schoolmember: {0})'.format(self.name))

    def tell(self):
        '''Вывести информацию'''
        print('Имя: "{0}", возраст: "{1}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    def __init__(self, name: str, age: int, salary: int):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))


class Student(SchoolMember):
    def __init__(self, name: str, age: int, marks: int):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))


t = Teacher('Mary', 32, 40000)
s = Student('Tom', 18, 70)

print()

members = [t, s]
for m in members:
    m.tell()

















