class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calc(self):
        return int((self.__length * self.__width * 125) / 1000)


road_a_b = Road(30000, 20)
print(f"Для покрытия дороги от пункта А до пункта Б надо {road_a_b.calc()} тонн асфальта.")

