class ValError(Exception):
    def __init__(self, txt):
        self.txt = txt


def make_int(s):
    if not s.isdigit():
        raise ValError('Вы ввели не число')

    return int(s)


print("Введите делимое и делитель")
n, m = input(), input()

n = make_int(n)
m = make_int(m)

if m == 0:
    raise ValueError("Не корректная операция, деление на ноль.")

print(f"Результат вычисления {n}/{m}={n/m}")
