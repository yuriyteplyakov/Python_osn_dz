def data_person(name, firstname, year_birthday, city, email, phone_number):
    return print(f'Вот ваши данные: {name}, {firstname}, {year_birthday}, {city}, {email}, {phone_number}')

n = input('Введите свое имя: ')
f = input('Введите фамилию: ')
y = input('Введите год рождения: ')
c = input('Введите город в котором проживаете: ')
e = input('Введите свой email: ')
p = input('Введите свой номер телефона: ')

data_person(name=n, firstname=f, year_birthday=y, city=c, email=e, phone_number=p)