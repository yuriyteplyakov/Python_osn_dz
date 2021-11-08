from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5

class Suit(Clothes):
    def __init__(self, H):
        self.H = H

    @property
    def consumption(self):
        return 2 * self.H + 0.3

    def sum_consumption(self, list_siuts):
        a = 0
        for suit in list_siuts:
            a += suit.consumption
        return a

coat = Coat(36)
costume_1 = Suit(2.5)
costume_2 = Suit(2.4)
costume_3 = Suit(1.32)
costume_4 = Suit(1.5)
costume_5 = Suit(2.7)
list_costumes = [costume_1, costume_2, costume_3, costume_4, costume_5]
print(coat.consumption)
print(costume_1.consumption)
print(costume_2.consumption)
print(costume_3.consumption)
print(costume_4.consumption)
print(costume_5.consumption)
print(costume_2.sum_consumption(list_costumes))