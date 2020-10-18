import sys


def fact(n):
    if n == 0:
        yield 1
    else:
        m = 1
        for i in range(1, n):
            m *= i
            yield m


if len(sys.argv) != 2:
    print(f"Было введено не верное количество параметров. ({len(sys.argv)-1})")
else:
    try:
        _, numb = sys.argv
        numb = int(numb)
        for el in fact(numb):
            print(el)
    except ValueError:
        print(f"Параметр должен быть числовым ({numb})")

