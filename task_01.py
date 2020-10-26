import time


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый', 'желтый']

    def rinning(self):
        start = time.time()
        time.sleep(2)
        color_number = 0

        # запускаем светофор на одну минуту
        while time.time() - start < 60:
            print(self.__color[color_number])
            time.sleep(2 if color_number % 2 else 7)

            color_number = (color_number + 1) % 4
        return


tl = TrafficLight()
tl.rinning()
