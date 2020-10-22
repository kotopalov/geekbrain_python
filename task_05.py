import random

fi_name = 'task_05.txt'
fo_name = 'task_05.txt'


def generate_file(f_name):
    fo = open(f_name, "w", encoding="utf8")
    print(" ".join(map(str, [random.randrange(0, 10000) for _ in range(500)])), file=fo)
    fo.close()


def calc_sum(f_name):
    with open(f_name, "r", encoding="utf8") as fi:
        s = fi.readline()
        try:
            print(f'Сумма чисел = {sum(map(int, (s.split())))}')
        except:
            print('Содержимое файла повреждено')


generate_file(fo_name)
calc_sum(fi_name)
