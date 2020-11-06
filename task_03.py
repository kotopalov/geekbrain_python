class ValError(Exception):
    def __init__(self, txt):
        self.txt = txt


def make_int(s: str) -> int:
    is_sign_minus = False

    if s[0] == '-':
        is_sign_minus = True
        s = s[1:]

    if not s.isdigit():
        raise ValError('Введенные тескт не является числом')

    return int(s) * (-1 if is_sign_minus else 1)


arr = []

# заполняем список данными введенными пользователем
while True:
    print("Введите новое значение или нажмите ВВОД для выполнения программы: ", end='')
    s = input()

    if s == '':
        break

    try:
        n = make_int(s)
    except ValError as err:
        print(err)

    arr.append(s)

print(arr)

