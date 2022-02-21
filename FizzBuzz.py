
intemp = int(input('Введите целое число - '))
# print(int(intemp))

if intemp % 3 == 0 and intemp % 5 == 0:
    print('FizzBuzz')
elif intemp % 3 == 0:
    print('Fizz')
elif intemp % 5 == 0:
    print('Buzz')
else:
    print('Чот не то о_О')


