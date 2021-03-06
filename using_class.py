class Person:
    '''Тут мы как бы пишет ля-ля тополя про сам класс.'''

    population = 0

    def __init__(self, fname: str, lname: str, old: int):
        '''Инициализация данных.
        Вызывается первым делом при создании экземпляра класса'''
        self.name1 = fname
        self.name2 = lname
        self.age = old

        Person.population += 1

    def __del__(self):
        '''Вызывается при удалении объекта - экземпляра класса'''
        print(f'{self.name1} ушел, увы :(')

        Person.population -= 1

        if Person.population == 0:
            print(f'Конец программы, все ушли')

    def say_hi(self) -> str:
        '''Крутая функция расскажет о тебе.'''
        return f'Hi, I\'m {self.name1}. I know you! Your Last name is {self.name2}. Your age is {self.age}'

    @staticmethod       # Декоратор для ститичного метода класса
    def how_many():
        '''Выводит численность людей. Необходимо указать, что это статический метод класса.
        Делается вот так после функции: how_many = staticmetod(how_many)'''
        print(f'Сейчас у нас в гостях - {Person.population}')
    # how_many = staticmethod(how_many)

# ========================================================================================================


print(f'\n{Person.say_hi.__doc__}')
# print(Person.__init__.__annotations__)      # Выводит аннотацию к magic method __init__
# print(Person.say_hi.__annotations__)

AndGr = Person('Andrey', 'Grachev', 30)
print(AndGr.say_hi())
# print(f'Пополяция людей достигла - {AndGr.population}')
Person.how_many()

YuriLop = Person('Yuri', 'Lopuhin', 32)
print(YuriLop.say_hi())
Person.how_many()

AlekseyZol = Person('Aleksey', 'Zolotuhin', 34)
print(AlekseyZol.say_hi())
Person.how_many()
