class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'Запуск отрисовки'
class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'
class Pensil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'
class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'

pen = Pen('Ручкой')
print(pen.draw())
pensil = Pensil('Карандашом')
print(pensil.draw())
handle = Handle('Маркером')
print(handle.draw())