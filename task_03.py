class Worker:
    name = ''
    surname = ''
    position = ''
    _income = dict()

    def __init__(self,  name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


w1 = Position("Alex", "Ton", "dev", 20000, 15000)

print(w1.get_full_name(), '-', w1.get_total_income())
print('Позиция - ', w1.position)
try:
    # в пределах одного модуля можно доступаться
    print('Доход - ', sum(w1._income.values()))
except:
    print('Нет доступа к защищенным данным')
