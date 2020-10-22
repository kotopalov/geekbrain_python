nums = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}


def transl(s):
    return nums.get(s, s)


def transform(s):
    arr = s.split()
    arr[0] = transl(arr[0])
    return ' '.join(arr)


fi_name = 'task_04_i.txt'
fo_name = 'task_04_o.txt'

fo = open(fo_name, "w", encoding="utf8")

with open(fi_name, "r", encoding="utf8") as fi:
    s = fi.readline()
    while s:
        s1 = transform(s)
        print(s1, file=fo)

        s = fi.readline()

fo.close()
