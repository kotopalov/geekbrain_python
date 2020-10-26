import random


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    direction = ''

    def __init__(self, name, color, is_police):
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.direction == '':
            print('Авто не может двигатья без направления.')
            return

        self.speed = random.randint(20, 120)

    def stop(self):
        self.speed = 0
        print(f'Авто {self.name} остановилось.')

    def turn(self, direction):
        self.direction = direction

    def show_speed(self):
        print(f"Скорость авто: {self.speed} в направлении {self.direction}")


class TownCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, False)

    def show_speed(self):
        print(f"Скорость авто: {self.speed}")
        if self.speed > 60:
            print("ВНИМАНИЕ! Скорость превышает разрешеную (60)")


class WorkCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, False)

    def show_speed(self):
        print(f"Скорость авто {self.name}: {self.speed}")
        if self.speed > 40:
            print("ВНИМАНИЕ! Скоросто приввышает разрешенную (40)")


class SportCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, False)


class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, True)


directions = ['Север', 'Восток', 'Юг', 'Запад']

cars = dict()
cars["Town"] = TownCar("Ока", "Красный")
cars["Work"] = WorkCar("ЗИЛ", "Синий")
cars["Sport"] = SportCar("Мустанг", "Зеленый")
cars["Police"] = PoliceCar("Калина", "Белый")

# авто не поедет без направления
cars["Police"].go()

for _ in range(10):
    for car in cars.values():
        car.turn(directions[random.randint(0, len(directions)-1)])
        car.go()
        car.show_speed()


for car in cars.values():
    car.stop()
