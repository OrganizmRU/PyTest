class ShortInputException(Exception):
    '''Пользовательский класс исключения'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('Введите текст: ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # Здесь может происходить обычная работа
except EOFError:
    print('\nВвод прерван комбинацией Ctrl-D')
except ShortInputException as ex:
    print('ShortInputException: длина введенной строки {0}, а ожидалось {1}'.format(ex.length, ex.atleast))
else:
    print('Не было исключений')