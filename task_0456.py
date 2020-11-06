class ValError(Exception):
    def __init__(self, txt):
        self.txt = txt


def to_int(str):
    try:
        n = int(str)
    except:
        raise ValError("Введенное значение не число.")
    return n


class OrgTypes:
    printer = 'принтер'
    scaner = 'сканер'
    xerox = 'ксерокс'


class Org:
    def __init__(self, firm_name: str, type: OrgTypes, cost: int):
        self.firm_name = firm_name
        self.type = type
        self.cost = cost


class PrinterType:
    laser = "лазерный"
    jet = "струйный"


class Printer(Org):
    def __init__(self, firm_name: str, cost: int, printer_type: PrinterType):
        Org.__init__(self, firm_name, OrgTypes.printer, cost)
        self.printer_type = printer_type

    def set_printer_prop(self, printer_type: PrinterType):
        self.printer_type = printer_type

    def __str__(self):
        return f'Марка-{self.firm_name}, тип-{self.printer_type}, цена-{self.cost}'

    @classmethod
    def create(cls):
        t = input("Введите тип принтера: 1-Лазерный, 2-Струйный\n")
        if t == '1':
            type = PrinterType.laser
        elif t == '2':
            type = PrinterType.jet
        else:
            raise ValError('Введен неверный тип принтера.')

        firm = input("Введите производителя:")
        cena = to_int(input("Введите цену:"))

        return Printer(firm, cena, type)


class Scaner(Org):
    def __init__(self, firm_name: str, cost: int, dpi):
        Org.__init__(self, firm_name, OrgTypes.scaner, cost)
        self.dpi = dpi

    def __str__(self):
        return f'Марка-{self.firm_name}, dpi-{self.dpi}, цена-{self.cost}'

    def set_scaner_prop(self, dpi: int):
        self.dpi = dpi

    @classmethod
    def create(cls):
        firm = input("Введите производителя:")
        dpi = to_int(input("Введите разрешение сканера:"))
        cena = to_int(input("Введите цену:"))

        return Scaner(firm, cena, dpi)


class Xerox(Printer, Scaner):
    def __init__(self, firm_name: str, cost: int):
        Org.__init__(self, firm_name, OrgTypes.xerox, cost)
        self.printer_type = 0
        self.scaner_type = 0

    def __str__(self):
        return f'Марка-{self.firm_name}, dpi-{self.dpi}, тип-{self.printer_type}, цена-{self.cost}'

    @classmethod
    def create(cls):
        firm = input("Введите производителя:")
        dpi = to_int(input("Введите разрешение сканера:"))
        t = input("Введите тип принтера: 1-Лазерный, 2-Струйный\n")
        if t == '1':
            type = PrinterType.laser
        elif t == '2':
            type = PrinterType.jet
        else:
            raise ValError('Введен неверный тип принтера.')
        cena = to_int(input("Введите цену:"))

        x = Xerox(firm, cena)
        x.set_printer_prop(type)
        x.set_scaner_prop(dpi)

        return x


class Sklad:
    def __init__(self):
        self.racks = dict()
        self.racks[OrgTypes.printer] = []
        self.racks[OrgTypes.scaner] = []
        self.racks[OrgTypes.xerox] = []

    def put_article(self, article, count):
        self.racks[article.type].append([article, count])

    def get_article(self, type: OrgTypes, count: int):
        pass

    def cout_article(self, type: OrgTypes):
        pass

    def show_by_type(self, type):
        if len(self.racks[type]) == 0:
            print(f"Стелаж '{type}' пуст")
        else:
            print(f"Стелаж '{type}' содержит:")
            for el in self.racks[type]:
                print(f"  {el[0]}: {el[1]} шт.")

    def content(self):
        self.show_by_type(OrgTypes.printer)
        self.show_by_type(OrgTypes.scaner)
        self.show_by_type(OrgTypes.xerox)


def put(skl: Sklad):
    while True:
        t = input("\nКакую технику хотите добавить?\n  1 - Принтер\n" + \
                  "  2 - Сканер\n  3 - Ксерокс\n  '' - выход\n")

        if t == "":
            raise ValError("Пользователь отменил ввод")
        elif t == "1":
            art = Printer.create()
        elif t == "2":
            art = Scaner.create()
        elif t == "3":
            art = Xerox.create()

        count = to_int(input("Введите количество:"))
        skl.put_article(art, count)


def get(skl: Sklad):
    pass


skl = Sklad()
while True:
    act = input("Выберите нужное действие:\n  1 - Остаток склада\n"+ \
                "  2 - Добавить технику\n  3 - Продать технику\n"+ \
                "  0(или пустое значение) - выход\n")

    if act == '0' or act == '':
        break
    elif act in ['1', '2', '3']:
        try:
            if act == '1':
                skl.content()
            if act == '2':
                put(skl)
            if act == '3':
                get(skl)
        except ValError as err:
            print("ВНИМАНИЕ: Прошлое действие было прервано по причине: " + err.txt)
    else:
        print(f"ОШИБКА: действие '{act}' не известно.")
