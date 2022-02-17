ab = {'Swaroop': '+7-917',
      'Larry': '+7-927',
      'Mat': '+7-937',
      'Nik': '+7-999'
      }
print('Номер Swaroop\'а -', ab['Swaroop'])

del ab['Nik']

print('В адресной книге {} контакта'.format(len(ab)))

for name, number in ab.items():
      print('Контакт {} с адресом {}'.format(name, number))

ab['Max'] = '+7-905'

if 'Max' in ab:
      print('Номер Макса - ', ab['Max'])



