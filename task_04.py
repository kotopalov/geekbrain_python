print("Введите предложение: ", end='')
e = input()

arr = e.split()

for i, s in enumerate(arr):
    print(f'{i+1}: {s[:10]}')
