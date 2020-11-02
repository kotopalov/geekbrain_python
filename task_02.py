from abc import ABC, abstractmethod


class Cothes(ABC):
    @abstractmethod
    def piece_of_cloth(self):
        """Возвращает нужное количество тркани."""
        pass


class __Cothes(ABC):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 0:
            self.__size = 0
        else:
            self.__size = size


class Coat(Cothes, __Cothes):

    @property
    def piece_of_cloth(self):
        return self.size / 6.5 + 0.5


class Suit(Cothes, __Cothes):

    @property
    def piece_of_cloth(self):
        return self.size * 2 + 0.3


# Заказы на пошив одежды
d = dict()
d['Alex'] = Coat(4)
d['Bob'] = Suit(11)
d['Hank'] = Coat(5)


print("На пошив необходимо ткани:", sum([c.piece_of_cloth for c in d.values()]))
