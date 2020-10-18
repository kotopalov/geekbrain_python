from functools import reduce


def my_multiplication(prev_el, el):
    return prev_el * el


print(reduce(my_multiplication, range(100, 1000+1, 2)))
