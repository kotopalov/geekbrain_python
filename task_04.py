n = int(input())

max_k = 0
while n > 0:
    k = n % 10
    if max_k < k:
        max_k = k

    n = n // 10

print(max_k)
