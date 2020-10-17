def int_func(w):
    return w.title()


def leave_small_latin(w):
    arr = []
    for s in w:
        if 97 <= ord(s) <= 122:
            arr.append(s)

    return ''.join(arr)


def transform(sent):
    arr = sent.split()
    arr_new = []
    for s in arr:
        s2 = int_func(leave_small_latin(s))
        if s2 != '':
            arr_new.append(s2)

    return ' '.join(arr_new)


print("Введите предложение")
sent = input()
sent = transform(sent)
print("Итоговое предложение:", sent)
