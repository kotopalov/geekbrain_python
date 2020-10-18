def only_bigger(arr):
    return [arr[n] for n in [i for i in range(1, len(arr))] if arr[n-1] < arr[n]]


print(only_bigger([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]))
