import sys

def count_salary(h, r, b):
    return round(h * r + b, 2)


if len(sys.argv) != 4:
    print(f"Было введено не верное количество параметров. ({len(sys.argv)-1})")
else:
    try:
        _, hours, rate, bonus = sys.argv
        hours = float(hours)
        rate = float(rate)
        bonus = float(bonus)
        s = count_salary(hours, rate, bonus)
        print(f'Зарплата сотрудника равна: {s:.2f}')
    except ValueError:
        print(f"Все параметры должны быть числами ({sys.argv[1:]})")
