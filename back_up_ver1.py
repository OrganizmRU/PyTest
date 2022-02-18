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
source = ['D:\\for_backup']
print('source - ', source)

target_dir_for_backup = 'D:\\'
print('target_dir', target_dir_for_backup)

target = target_dir_for_backup + os.sep + time.strftime('%Y%m%d_%H%M%S') + '.zip'
print('target command', target)

zip_command = "zip -p {0} {1}".format(target, ''.join(source))
print(zip_command)

