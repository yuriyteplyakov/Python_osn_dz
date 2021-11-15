class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def type(cls, day_month_year):
        date = []
        for i in day_month_year.split():
            date.append(i)
        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31 and 1 <= month <= 12 and 0 <= year <= 2021:
            return f'Все верно!'
        else:
            return f'Неправильный формат даты'



print(Date.valid(453, 2, 2021))
print(Date.valid(23, 97, 1387))
print(Date.valid(14, 2, 2007))
print(Date.type('25 2 2021'))
