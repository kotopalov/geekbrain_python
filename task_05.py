def take_new_data():
    print("Введите последовательность чисел через пробел.")
    print("'Q' как отдельное слово будет означать выход из программы")
    print("любые другие буквы, символы или не правильный ввод будет игнорироваться.")
    s = input()
    a = s.split()

    arr = []
    is_exit = False
    for el in a:
        if el.upper() == "Q":
            is_exit = True
            break
        else:
            try:
                i = int(el)
            except:
                break

            arr.append(i)

    return is_exit, arr


def collect_data_from_user():
    sum_t = 0
    while True:
        is_exit, arr = take_new_data()

        s = sum(arr)
        sum_t += s

        print(f"{s}({sum_t})")

        if is_exit:
            break

    return sum_t


sum_t = collect_data_from_user()
print("Total sum:", sum_t)
