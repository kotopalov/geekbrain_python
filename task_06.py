from itertools import count, cycle

my_count = count(4)
my_cycle = cycle([next(my_count) for _ in range(5)])
print([next(my_cycle) for _ in range(15)])
