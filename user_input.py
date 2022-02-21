def reverse(text):
    return text[::-1]


def is_palindrom(text):
    return text == reverse(text)    # выводит false или true


A = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
a = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
_ = list('?!,. ')


something = list(input('Введите текст: '))
for i in something:
    for j in A:
        if i == j:
            something[something.index(i)] = a[a.index(j)]
    for j in _:
        if i == j:
            del something[something.index(i)]
    print(something)

# if (is_palindrom(something)):
#     print('да, это полиндром')
# else:
#     print('нет, это не палиндром')
