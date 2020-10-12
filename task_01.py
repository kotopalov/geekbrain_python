arr = [None, 'abc', 1, 1.1, [1, 2], {3, 4}, (5, 6), {"a": 1, "b": 2}]

# проверяем тип для каждого элемента
for el in arr:
    el_type = 'неизвестен'
    if type(el) == str:
        el_type = 'строка'
    elif type(el) == int:
        el_type = 'целое число'
    elif type(el) == float:
        el_type = 'вещественное число'
    elif type(el) == list:
        el_type = 'список'
    elif type(el) == set:
        el_type = 'множество'
    elif type(el) == tuple:
        el_type = 'кортеж'
    elif type(el) == dict:
        el_type = 'словарь'

    print(f"Элемент '{el}' имеет тип: {el_type}")

# решение №2
print("решение №2")

dTypes = {int: 'целое число',
    str: 'строка',
    float: 'вещественное число',
    list: 'список',
    set: 'множество',
    tuple: 'кортеж',
    dict: 'словарь'
          }

for el in arr:
    t = type(el)
    if t not in dTypes.keys():
        print(f"Тип элемента '{el}' не определен.")
    else:
        print(f"Элемент '{el}' имеет тип: {dTypes[t]}")
