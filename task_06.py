def calc_h(hs):
    t = 0
    n = 0
    for s in hs:
        if s.isnumeric():
            n = n * 10 + int(s)
        else:
            t += n
            n = 0

    return t


f_name = 'task_06.txt'
f = open(f_name, "r", encoding="utf8")

content = f.readlines()
f.close()

d = dict()
for s in content:
    subj, hs = s.split(":")
    d[subj] = calc_h(hs)

print(d)
