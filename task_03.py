class Organism:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Organism(self.cells + other.cells)

    def __sub__(self, other):
        return Organism(self.cells - other.cells if self.cells > other.cells else 0)

    def __mul__(self, other):
        return Organism(round(self.cells * other.cells))

    def __truediv__(self, other):
        return Organism(0 if other.cells == 0 else round(self.cells / other.cells))

    def make_order(self):
        if self.cells == 0:
            return 'Организм мертв'
        arr = ['*****' for _ in range(self.cells // 5)]
        rest = self.cells % 5
        if rest > 0:
            arr.append('*'*rest)
        return  '\n'.join(arr)
        #return '*****\n'*(self.cells // 5) + '*'*(self.cells % 5) + '\n'


print('--организм--\n' + (Organism(2) + Organism(3)).make_order() + '\n-----------')
print('--организм--\n' + (Organism(12) + Organism(2)).make_order() + '\n-----------')
print('--организм--\n' + (Organism(12) - Organism(3)).make_order() + '\n-----------')
print('--организм--\n' + (Organism(2) - Organism(2)).make_order() + '\n-----------')
print('--организм--\n' + (Organism(3) * Organism(2)).make_order() + '\n-----------')
print('--организм--\n' + (Organism(2) / Organism(6)).make_order() + '\n-----------')
print('--организм--\n' + (Organism(3) / Organism(2)).make_order() + '\n-----------')
