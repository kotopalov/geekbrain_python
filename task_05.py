my_list = [7, 5, 3, 3, 2]

# заполняем список данными введенными пользователем
while True:
    print("Введите новое число или нажмите ВВОД для выполнения программы: ", end='')
    s = input()
    if s == '':
        break

    # запиминаем знак числа
    sign = 1
    if s[0] == '-':
        s = s[1:]
        sign = -1

    n = sign
    if s.isdigit():
        n *= int(s)
    elif s.replace('.', '').isdigit():
        n *= float(s)
    else:
        print('Введены не правильные данные.')
        continue

    added = False
    for i, el in enumerate(my_list):
        if el < n:
            my_list.insert(i, n)
            added = True
            break

    if not added:
        my_list.append(n)

print(f'Итоговый список: {my_list}')

