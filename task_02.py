"""
Тут есть, тонкий спорный момент
когда в файле последняя строка пустая.
Если расматривать строки как Пайтон, когда перенос строки
это часть предыдущей строки то все ок строк 3 (ask_02.txt)
но по факту, если есть перенос строки то и есть новая строка.
Так что строк не 3, а 4. Это не сложно обработать
но не знал считается ли последняя пустая строка
"""

f_name = 'task_02.txt'
f = open(f_name, "r", encoding="utf8")

content = f.readlines()
f.close()

print(f"В файле {f_name} находится {len(content)} строк.")
for i, s in enumerate(content):
    print(f"В строке {i+1} находится {len(s.split())} слов.")


print("\nВариант 2.")
with open(f_name, "r", encoding="utf8") as f:
    s = f.readline()
    i = 1
    while s:
        print(f"В строке {i} находится {len(s.split())} слов.")
        s = f.readline()
        i += 1
