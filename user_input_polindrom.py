def reverse(text: list) -> list:
    return text[::-1]                  # реверсирует весь список


def is_palindrom(text: list) -> bool:
    if text != []:
        return text == reverse(text)   # выводит false или true
    else:
        return False


A = tuple('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
a = tuple('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
_ = tuple('?!,. ')

try:
    text_in = list(input('Введите текст: '))
    text_edit = []
except EOFError:
    print('\nВвод прерван комбинацией Ctrl-D')
except NameError:
    print('\nНеверное имя функции')
except KeyboardInterrupt:
    print('\nВы отменили операцию')
else:
    print('\nНет ошибок')


# print('! -', text_in)
for i, val in enumerate(text_in):
    for j in range(len(A)):
        if text_in[i] == A[j]:
            text_edit.append(a[j])
        elif text_in[i] == a[j]:
            text_edit.append(text_in[i])
print('? -', text_edit)

if is_palindrom(text_edit):
    print('\nда, это полиндром')
else:
    print('\nнет, это не палиндром')
