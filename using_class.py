class Person:
    '''Тут мы как бы пишет ля-ля тополя про сам класс'''

    def __init__(self,
                 fname: str,
                 lname: str,
                 age: int):
        self.name1 = fname
        self.name2 = lname
        self.age = age

    def sayHi(self):
        print('Hi, {}. I know you!'.format(self.name1))
        print('Your Last name is', self.name2)
        print('Your age is', self.age)

# =======================================================================


And = Person('Andrey', 'Grachev', 30)
And.sayHi()

print(Person.__doc__)

