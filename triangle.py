choo = (input('Выберите ваш треугольник:\n1. Нижний\n2. Верхний\n> '))

if choo == '1':
    line_num = int(input('Введите длинну нижней грани треугольника: '))
    for line in range(1, line_num+1):
        print('*' * line)

elif choo == '2':
    line_down = int(input('Введите длину верхней грани треугольника: '))
    for rev in range(line_down, 0, -1):
        print('*' * rev)
else:
    print('You need choose something')