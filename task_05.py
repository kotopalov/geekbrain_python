class Stationery:
    title = 'Неопределено'

    def draw(self):
        print(f'Запуск отрисовки предмета {self.title}.')


class Pen(Stationery):
    title = 'Ручка'

    def draw(self):
        super().draw()
        print('   ________')
        print(' _/________________________')
        print('(__________________________)=>')
        print('')


class Pencil(Stationery):
    title = 'карандаш'

    def draw(self):
        super().draw()
        print(' ________________________')
        print('|________________________\\_')
        print('|________________________/ ')
        print('')


class Handle(Stationery):
    title = 'маркер'

    def draw(self):
        super().draw()
        print(' --------------------\___')
        print('(                    (___\\')
        print(' --------------------/')
        print('')


sts = [Pen(), Pencil(), Handle()]
for x in sts:
    x.draw()

