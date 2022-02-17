def total(a=5, *numbers, **phonebook):
    print('a', a)

    # проход ко всем элементам кортежа
    for single_item in numbers:
        print('single_item', single_item)

    # проход ко всем элементам словаря
    for first_rapt, second_part in phonebook.items():
        print(first_rapt, second_part)


print(total(10, 1, 2, 3, Jack=1123, John=2234, Inge=3345))
