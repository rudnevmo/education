import math

while True:

    ans = input('Выберете необходимую функцию: +, -, *, /, ^, sin, cos, tan (exit для выхода): ')
    if ans == '/' or ans == '+' or ans == '-' or ans == '*':
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
    elif ans == '^':
        a = float(input('Введите число: '))
        b = float(input('Введите степень: '))
    elif ans == 'sin' or ans == 'cos' or ans == 'tan':
        a = float(input('Введите значение ' + str(ans) + ' в радианах: '))
    else:
        print('Нужно выбрать что-то из предложенных функций)')

    if ans == '/':
        if b == 0:
            print('На ноль делить нельзя')
            continue
# todo Как закрыть цикл без ошибки
        c = a / b
        print('Результат деления: ' + str(c))

    elif ans == '+':
        c = a + b
        print('Результат сложения: ' + str(c))

    elif ans == '*':
        c = a * b
        print('Результат умножения: ' + str(c))

    elif ans == '-':
        c = a - b
        print('Результат вычитания: ' + str(c))

    elif ans == '^':
        c = a ** b
        print('Результат возведения в степенm: ' + str(c))

    elif ans == 'sin':
        c = math.sin(a)
        print('Синус ' + str(a) + ' равен ' + str(c))

    elif ans == 'cos':
        c = math.cos(a)
        print('Косинус ' + str(a) + ' равен ' + str(c))

    elif ans == 'tan':
        c = math.tan(a)
        print('Тангенс ' + str(a) + ' равен ' + str(c))

    if ans == 'exit':
        break