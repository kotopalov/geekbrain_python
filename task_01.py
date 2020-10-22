f_name = 'task_01.txt'
f = open(f_name, "w", encoding="utf8")

print(f"Введите последовательно строки для записи в файл '{f_name}'")
print("Для окончания ввода введите пустую строку")
while True:
    print("Введите строку: ")
    s = input()

    if s == '':
        break

    print(s, file=f)

f.close()
