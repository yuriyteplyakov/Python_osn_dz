class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} тронулась с места.'
    def stop(self):
        return f'Машина {self.name} остановилась.'
    def turn(self, direction):
        return f'Машина {self.name} повернула {direction};'
    def show_speed(self):
        return f'Текущая скорость {self.speed} км/ч;'
class TownCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Текущая скорость {self.speed} км/ч. Превышение скорости! Лимит 60 км/ч!;'
        else:
            return f'Текущая скорость {self.speed} км/ч - Скорость не превышена;'
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Текущая скорость {self.speed} км/ч. Превышение скорости! Лимит 40 км/ч!;'
        else:
            return f'Текущая скорость {self.speed} км/ч - Скорость не превышена;'
class PoliceCar(Car):
    pass

town = TownCar('Ford', 90, 'green', False)
sport = SportCar('Tesla', 300, 'Black', False)
work = WorkCar('Rolls-Royce ', 20, 'Rose-gold', False)
police = PoliceCar('Lada Priora', 1000000, 'Red', True)

print('1:\n' + town.go(), town.show_speed(),'\n' + town.turn('вправо'),'\n' + town.turn('влево'),'\n' + town.stop())
print('2:\n' + sport.go(), sport.show_speed(),'\n' + sport.turn('влево'),'\n' + sport.turn('влево'),'\n' + sport.stop())
print('3:\n' + work.go(), work.show_speed(),'\n' + work.turn('вправо'),'\n' + work.turn('назад'),'\n' + work.stop())
print('4:\n' + police.go(), police.show_speed(),'\n' + police.turn('вправо'),'\n' + police.turn('влево'),'\n' + police.stop())
