class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight_meter_square = 25 #расход асфальта на 1 кв.м. при толщине слоя 1 см равен 25 кг
        self.height = float(input('Введите толщину асфальта в метрах: '))
    def weight(self):
        return self._length * self._width * self.weight_meter_square * self.height

l = float(input('Введите требуемую длину асфальта в метрах: '))
w = float(input('Введите требуемую ширину асфальта в метрах:'))
r = Road(l, w)
print(f'Масса асфальта при введенных данных {r.weight()} кг')