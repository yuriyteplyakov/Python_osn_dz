class MyException(Exception):
    def __init__(self, text):
        self.text = text


try:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    if b == 0:
        raise MyException("Вы не можете делить на ноль!")
    c = a / b
    print(c)
except Exception as e:
    print(e)
