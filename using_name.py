def print_hi():
    if __name__ == '__main__':
        print('Эта программа запущена сама по себе. Меня зовут ' + __name__)
    else:
        print('Меня портировали в другой модуль. Меня зовут ' + __name__)