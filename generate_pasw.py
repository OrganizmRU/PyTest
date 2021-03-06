import random


def generate_password(m):
    for i in range(150):
        pasw = ''.join([random.choice(random.choice(letter)) for _ in range(m)])
        if len(pasw) == len(set(pasw)): # Проверка на повторяющиеся символы
            return pasw                 # Нет повторений -> вернуть ответ
        else:
            pass


def main(n: int, m: int):
    password = []
    for _ in range(n):
        password.append(generate_password(m))
        while password[-1] in password[:-1]:
            password[-1] = generate_password(m)
    return password

# ======================================================================================

letter = ['ABCDEFGHJKLMNPQRSTUVWXYZ',
          'abcdefghijkmnpqrstuvwxyz',
          '23456789',
          '!@#$%^&*()_+~']

print("Случайный пароль из 7 символов:", generate_password(7))
print("\n10 случайных паролей длиной 15 символов:\n")
print(*main(10, 15), sep="\n")
