class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage':int(wage), 'bonus':int(bonus)}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name}, {self.surname}, {self.position}'
    def get_total_income(self):
        return f'(доход с учетом премии - {self._income["wage"] + self._income["bonus"]} руб)'

p = Position('Petr', 'Perviy', 'pravitel', '43773', '32')
p_1 = Position('Vasya', 'Stepanov', 'Slesar', '12358', '347')
p_2 = Position('Katya', 'Strelcova', 'letchik', '126654', '2356')
p_3 = Position('Ivan', 'Mironov', 'Kassir', '8996437', '23574775')
print(p.get_full_name(), p.get_total_income())
print(p_1.get_full_name(), p.get_total_income())
print(p_2.get_full_name(), p.get_total_income())
print(p_3.get_full_name(), p.get_total_income())