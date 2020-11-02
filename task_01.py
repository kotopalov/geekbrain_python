from functools import reduce

class MyMatrix:
    def __init__(self, m):
        self.matrix = m

    def __add__(self, other):
        return MyMatrix(self.mult_matrixes(self.matrix, other.matrix))

    def __str__(self):
        return "\n".join([" ".join([f'{j:5}' for j in i]) for i in self.matrix])

    # возвращает элемент массива по первому листа
    # если индекс вне диапазона размера листа возвращает 0
    def get_one_d_matrix_element(self, m, i):
        return m[i] if i<len(m) else 0

    # складывает элементы в одинаковых позициях массевов
    def mult_elms(self, m1, m2, i):
        return (self.get_one_d_matrix_element(m1, i) +
                self.get_one_d_matrix_element(m2, i))

    # складываем одномерные массивы
    def mult_one_d_matrixes(self, m1, m2):
        return [self.mult_elms(m1, m2, i) for i in range(max(len(m1), len(m2)))]

    # возвращает одномерный массив по первому интексу матрицы
    # если индекс вне диапазона размера матрицы возвращает пустой лист
    def get_one_d_matrix(self, m, i):
        return m[i] if i<len(m) else []

    # складываем маотрицы по строчно
    def mult_matrixes(self, m1, m2):
        return [self.mult_one_d_matrixes(self.get_one_d_matrix(m1, i),
                                         self.get_one_d_matrix(m2, i))
                for i in range(max(len(m1), len(m2)))]


g_m1 = MyMatrix([[1, 2], [2, 3]])
g_m2 = MyMatrix([[2, 3], [3, 4], [3, 4]])
print((g_m1 + g_m2))
