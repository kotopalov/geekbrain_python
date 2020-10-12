s = ''
arr = []

# заполняем список данными введенными пользователем
while True:
    print("Введите новое значение или нажмите ВВОД для выполнения программы: ", end='')
    s = input()
    if s == '':
        break

    arr.append(s)

print(arr)

for i in range(len(arr) // 2):
    arr[i*2], arr[i*2 + 1] = arr[i*2 + 1], arr[i*2]

print(arr)
