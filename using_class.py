class Person:
    '''Тут мы как бы пишет ля-ля тополя про сам класс'''

    def __init__(self,
                 fname: str,
                 lname: str,
                 age: int):
        self.name1 = fname
        self.name2 = lname
        self.age = age

    def say_hi(self) -> str:
        # print('Hi, {}. I know you!'.format(self.name1))
        # print('Your Last name is', self.name2)
        # print('Your age is', self.age)
        full = f'Hi, {self.name1}. I know you! Your Last name is {self.name2}. Your age is {self.age}'
        return full

# =======================================================================


print(f'\n{Person.__doc__}')

AndGr = Person('Andrey', 'Grachev', 30)
print(AndGr.say_hi())

# YuriLop = Person('Yuri', 'Lopuhin', 32)
# YuriLop.sayHi()

