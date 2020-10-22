f_name = 'task_03.txt'
f = open(f_name, "r", encoding="utf8")


# преобразовываем текстовый лист в в лист с данными
def pars(lst):
    arr = []
    for el in lst[1:]:
        el_lst = el.strip().split()
        try:
            arr.append([int(el_lst[0]), f"{el_lst[1]} {el_lst[2]}", float(el_lst[3])])
        except :
            print(f"Некорректные данные: '{el}'")

    return arr


cont = f.readlines()
f.close()

arr = pars(cont)

if len(arr) == 0:
    print("Файл испорчен или пустой.")
else:
    rsum = sum([el[2] for el in arr])
    cnt = len(arr)
    mean_sal = rsum / cnt

    print(f"Сотрудников в списке {cnt}.")
    print(f"Из них имеют оклад менее 20000.00:")
    for el in arr:
        if el[2] < 20000:
            print(f"{el[1]:15} {el[2]:12.2f}")

    print(f"\nСредний оклад составляет: {mean_sal:.2f}")
