import json


f_name = 'task_07_i.txt'
fo_name = 'task_07_o.txt'


with open(f_name, "r", encoding="utf8") as f:
    content = f.readlines()

d = dict()
arr_p = []
for s in content:
    arr = s.split()

    try:
        p = int(arr[2]) - int(arr[3])
    except:
        print(f"Не верные исходные данные: {s}")

    if p > 0:
        arr_p.append(p)

    d[arr[0]] = p

if len(d) > 0:

    arr = []
    arr.append(d)
    arr.append({'average_profit': round(sum(arr_p)/len(arr_p))})

    print(arr)

    with open(fo_name, "w", encoding="utf8") as f:
        json.dump(arr, f)
else:
    print(f"Не верные исходные данные")
