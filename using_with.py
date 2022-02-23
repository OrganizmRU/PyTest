with open('poem.txt') as f:         # после выполнения файл закроется автоматически
    for line in f:
        print (line, end='')