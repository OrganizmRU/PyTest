def reverse(text):
    return text[::-1]


def is_palindrom(text):
    return text == reverse(text)    # выводит false или true


A = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
a = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
_ = list('?!,. ')


text_in = list(input('Введите текст: '))
text_edit = []

print('! -', text_in)
for i, val in enumerate(text_in):
    for j in range(len(A)):
        if text_in[i] == A[j]:
            text_edit.append(a[j])
        elif text_in[i] == a[j]:
            text_edit.append(text_in[i])
print('? -', text_edit)

if (is_palindrom(text_edit)):
    print('да, это полиндром')
else:
    print('нет, это не палиндром')
