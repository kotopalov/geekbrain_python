class Data:
    def __init__(self, str_data: str):
        self.day, self.month, self.year = self.transform(str_data)
        if not self.is_data_correct(self.day, self.month, self.year):
            raise ValueError

    @classmethod
    def transform(cls, str_data: str) -> tuple:
        lst = str_data.split('-')
        if len(lst) != 3:
            raise ValueError
        if sum([not l.isdigit() for l in lst]) != 0:
            raise ValueError
        lst = list(map(int, lst))
        return lst[0], lst[1], lst[2]

    @staticmethod
    def is_data_correct(dd, mm, yy) -> bool:
        # нет надобности проверять год

        if not 1 <= mm <= 12:
            return False

        d = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if not 0 <= dd <= d[mm - 1]:
            return False
        # проверяем февраль высокосного года
        if mm == 2 and yy % 4 == 0 and dd == 29:
            return False

        return True


a = Data('311-12-11')
