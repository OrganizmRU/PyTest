import timeit
from datetime import datetime as DT

n = int(input('Введите целое число - '))

for i in range(n+1):
    print(i % 3 // 2 * 'Fizz' + i % 5 // 4 * 'Buzz' or i + 1)

# for i in range(1, n+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print('{0} - FizzBuzz'.format(i))
#     elif i % 3 == 0:
#         print(f'{i} - Fizz')
#     elif i % 5 == 0:
#         print(f'{i} - Buzz')
#     else:
#         print(i)

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

# start_time = DT.now()
# for i in range(1, 5000):
#     out = ''
#     if i % 3 == 0:
#         out += 'Fizz'
#     if i % 5 == 0 :
#         out += 'Buzz'
#     if out == '':
#         out = i
#     print(out)
# print(DT.now() - start_time)
