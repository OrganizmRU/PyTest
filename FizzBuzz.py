import timeit
from datetime import datetime


n = int(input('Введите целое число - '))

for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print('{0} - FizzBuzz'.format(i))
    elif i % 3 == 0:
        print(f'{i} - Fizz')
    elif i % 5 == 0:
        print(f'{i} - Buzz')
    else:
        print(i)

# for i in range(1, n+1):
#     out = ''
#     if i % 3 == 0:
#         out += 'Fizz'
#     if i % 5 == 0 :
#         out += 'Buzz'
#     if out == '':
#         out = i
#     print(out)

# =================================================================
# Сейчас посчитаем время выполнения кода модулем timeit

# code_to_test = """сюда вставляем код"""
# elapsed_time = timeit.timeit(code_to_test, number=100) / 100
# print(elapsed_time)

# =================================================================
# Сейчас посчитаем время выполнения кода модулем datetime

# start_time = datetime.now()
# for i in range(1, 5000):
#     out = ''
#     if i % 3 == 0:
#         out += 'Fizz'
#     if i % 5 == 0 :
#         out += 'Buzz'
#     if out == '':
#         out = i
#     print(out)
# print(datetime.now() - start_time)
