class Person:
    '''Тут мы как бы пишет ля-ля тополя про сам класс.'''

    population = 0

    def __init__(self,
                 fname: str,
                 lname: str,
                 age: int):
        '''Инициализация данных.'''
        self.name1 = fname
        self.name2 = lname
        self.age = age

        Person.population += 1

    def say_hi(self) -> str:
        '''Крутая функция расскажет о тебе.'''
        # print('Hi, {}. I know you!'.format(self.name1))
        # print('Your Last name is', self.name2)
        # print('Your age is', self.age)
        full = f'Hi, {self.name1}. I know you! Your Last name is {self.name2}. Your age is {self.age}'
        return full


# =======================================================================


print(f'\n{Person.say_hi.__doc__}')

AndGr = Person('Andrey', 'Grachev', 30)
print(AndGr.say_hi())
print(f'Пополяция людей достигла - {AndGr.population}')

YuriLop = Person('Yuri', 'Lopuhin', 32)
print(YuriLop.say_hi())
print(f'Пополяция людей достигла - {YuriLop.population}')
