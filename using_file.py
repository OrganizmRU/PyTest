poem = '''\
Программировать весело.
Если работа скучна,
Чтобы придать ей веселый тон - 
    задуши Питона'''

f = open('poem.txt', 'w')       # r-read, w-write, a-append
f.write(poem)
f.close()

f = open('poem.txt')

while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')

f.close()