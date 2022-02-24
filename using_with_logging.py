import os, platform, logging


# with open('poem.txt') as f:         # после выполнения файл закроется автоматически
#     for line in f:
#         print (line, end='')

print(platform.platform())
logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
target_file = 'D:\\Python\\PyTest' + os.sep + 'test.log'
print('Можем сохранить логи сюда - ', logging_file, '! А можем сюда -', target_file)
# print(os.getenv('HOMEDRIVE'))
# print(os.getenv('HOMEPATH'))
# print(os.getenv('APPDATA'))
# print(os.getenv('USERPROFILE'))

logging.basicConfig(filename=target_file, filemode='w', level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s')

logging.debug('Начало программы')
logging.info('Какие-то действия')
logging.warning('Программа умирает')
