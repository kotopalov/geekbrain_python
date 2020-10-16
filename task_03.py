def sum_2max(n1, n2, n3):
    a = [n1, n2, n3]
    a.remove(min(a))
    print(f"Sum{a}: {sum(a)}")


sum_2max(1, 2, 3)
sum_2max(2, 2, 3)
sum_2max(3, 3, 3)
sum_2max(4, 2, 3)
