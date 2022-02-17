# This is a sample Python script.

import using_name

print('1.', using_name.print_hi())


def print_hi():
    pr = ''
    if __name__ == '__main__':
        pr = 'Эта программа запущена сама по себе. Меня зовут ' + __name__
    else:
        pr = 'Меня портировали в другой модуль. Меня зовут ' + __name__
    return pr


print('2.', print_hi())


# import sys
#
# print('Аргументы командной строки: ')
# for i in sys.argv:
#     print(i)
#
# print('\n\nПеременная PythonPATH содержит', sys.path, '\n')

# import os
# print(os.__name__, 'Путь файла:', os.getcwd())
#
# print(__name__)
