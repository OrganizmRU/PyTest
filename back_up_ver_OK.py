import os
import time
# list_sep = dir(os)
# print(list_sep)
# for i in list_sep:
#     if i == 'sep':
#         print(list_sep.index(i))
#
# help(os)
#
# print(time.strftime('%Y%m%d_%H%M%S'))
#
# help(time)
# source = ['"C:\\My Documents"', 'C:\\Code']
source = ['D:\\for_backup']
print('source -', source)

target_dir_for_backup = 'D:\\backups'
print('target_dir -', target_dir_for_backup)

target_file = target_dir_for_backup + os.sep + time.strftime('%Y%m%d_%H%M%S') + '.zip'
# os.sep добавляет вместо себя разделитель ОС для пути
# time.strftime('%Y%m%d_%H%M%S') переводит кортеж времени в строку и возвращает в требуемом формате
print('target file -', target_file)

zip_command = "7z a {0} {1}".format(target_file, ' '.join(source))
# zip_command for cmd = 7z a D:\time*.zip D:\for_backup
# zip_command = "\"C:\\Program Files\\7-Zip\\7z.exe\" a -tzip -ssw -mx1 -r0 {0} {1}".format(target, ' '.join(source))
print(zip_command)

if os.system(zip_command) == 0:
    print('Ок, проверь архив в', target_dir_for_backup)
else:
    print('Ошибка, проверь код')
