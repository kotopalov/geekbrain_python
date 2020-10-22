def only_single(arr):
    return [n for n in arr if arr.count(n) == 1]


print(only_single([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]))
