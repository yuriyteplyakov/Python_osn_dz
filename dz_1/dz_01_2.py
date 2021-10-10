seconds = int(input("Введите время в секундах: "))
hours = seconds // 3600
minutes = (seconds - hours * 3600) // 60
seconds_ost = (seconds - hours * 3600) - minutes * 60
time = f"Это вот столько часов:{hours:02} минут:{minutes:02} секунд:{seconds_ost:02}"
print(time)

