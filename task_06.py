sklad = []
specs = ["наименование", "цена", "количество", "ед.из."]
var = 1

print("Выберите вариант и введите его номер:")
print("  1 - использовать стандартный набор параметров")
print(f"      [{', '.join(specs)}]")
print("  2 - ввести свои характеристики")
print("  (пустое значение соответствует варианту 1)")
while True:
    print(">", end='')
    s = input()
    if s == '':
        break
    elif s == '1':
        break
    elif s == '2':
        var = 2
        break
    else:
        print("введено не правильное значение повторите попытку")
        continue

print("var ", var)

# заполняем структуру данных пользователя
if var == 2:
    specs = []

    print("Инициализация структуры данных.")
    print("(пустая строка подразумеват окончание ввода)")
    while True:
        print("Введите новую характеристику товара: ")
        print(">", end='')
        s = input()
        if s == '':
            break

        if s in specs:
            print("Такая характеристика уже существует.")
            continue

        specs.append(s)

    print(specs)
    print("Структура данных:")

last_tov = 0
while True:
    print("Выберите одну из команд:")
    print(" 1 - добавить новый товар")
    print(" 2 - вывести список характеристик")
    print(" 3 - вывести структуру данных")
    print(" 4 - вывести аналитику товаров")
    print(" 0 - выход.")
    s = input()

    # выход из программы
    if s == '0':
        break

    # вывод списка характеристик
    elif s == '2':
        print("Список характеристик:")
        for i, el in enumerate(specs):
            print(f"{i}: {el}")

    # вывод структуры данных
    elif s == '3':
        if len(sklad) == 0:
            print("Данные еще не введены.\n")
        else:
            print("Структура данных:")
            for el in sklad:
                print(el)

    # вывод аналитики
    elif s == '4':
        if len(sklad) == 0:
            print("Данные еще не введены.\n")
        else:
            # создаем пустой список аналитики на основе характеристик
            # для хранения однотипных характеристик используем множество
            # для хранения тольуо уникальных характеристик
            analytic = dict()
            for sp in specs:
                analytic[sp] = set()

            # заполняем аналитику
            for el in sklad:
                for sp in specs:
                    analytic[sp].add(el[1][sp])

            # вывод аналитики
            for el in analytic:
                print(f"{el}: {analytic[el]}")

    # вывод нового товара
    elif s == '1':
        print("Введите данные для нового товара")
        print("(пустое значение - отмена ввода)")
        tov = dict()
        for i, sp in enumerate(specs):
            print(f"{i}.{sp}: ", end='')
            t = input()

            # отмена ввода
            if t == '':
                tov = dict()
                break

            tov[sp] = t

        # сохраняем товар
        if len(tov) != 0:
            last_tov += 1
            sklad.append(tuple([last_tov, tov]))

    else:
        print("не верные данные, сделайте свой выбор еще раз ")
        continue
