def get_XY():
    x = 0
    y = 0
    print("Введите два числа через пробел или запятую. Или пустую строку для выхода.")
    while True:
        s = input()
        if s == '':
            print('Отмена ввода')
            return False, 0, 0

        s = s.replace(',', ' ')
        strs = s.split(' ')
        while '' in strs:
            strs.remove('')

        if len(strs) != 2:
            print("неверно введенные данные! Попробуйте еще раз.")
            continue

        try:
            x = int(strs[0])
            y = int(strs[1])
        except:
            print("Были введены не числоые значения. Попробуйте еще раз.")
            continue

        break

    return True, x, y


def div(a, b):
    if b == 0:
        return 0

    return a / b


is_all_fine, x, y = get_XY()
if is_all_fine:
    z = div(x, y)
    if z == 0:
        print("Деление на ноль не возможно.")
    else:
        print(f"Результат деления: {z}")
