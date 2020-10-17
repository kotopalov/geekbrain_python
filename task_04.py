def get_an():
    x = 0
    y = 0
    print("Введите два числа (действительное положительное число x")
    print("и целое отрицательное число y) через запятую.")
    print("Или пустую строку для выхода.")
    while True:
        s = input()
        if s == '':
            print('Отмена ввода')
            return False, 0, 0

        s = s.replace(' ', '')
        strs = s.split(',')

        if len(strs) != 2:
            print("неверно введенные данные! Попробуйте еще раз.")
            continue

        try:
            x = int(strs[0])
            y = int(strs[1])
        except:
            print("Были введены не числоые значения. Попробуйте еще раз.")
            continue

        if x <= 0:
            print("Первое число не может быть отрицательным или 0. Попробуйте еще раз.")
            continue

        if y >= 0:
            print("Второе число не может быть положительным или 0. Попробуйте еще раз.")
            continue

        break

    return True, x, y


def exp(a, n):
    print("Вариант 1:", a**n)


def exp2(a, n):
    n = (-1 * n)
    print("Вариант 2:", 1/a**n)


def exp3(a, n):
    n = (-1 * n)
    e = 1

    for i in range(n):
        e *= a

    print("Вариант 3:", 1/e)


is_all_fine, x, y = get_an()
if is_all_fine:
    exp(x, y)
    exp2(x, y)
    exp3(x, y)

