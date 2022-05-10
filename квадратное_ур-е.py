print('Уравнение ax^2 + bx + c = 0')

a = int(input('Enter the A number: '))
b = int(input('Enter the B number: '))
c = int(input('Enter the C number: '))

D = (b**2 - 4 * a * c)

print('Дискриминант равен: ' + str(D))

if D > 0:
    print('Корней будет два')
    x1 = (-b + D ** 1/2) / (2 * a)
    x2 = (-b - D ** 1/2) / (2 * a)
    print('x1 = ' + str(x1) + ' and x2 = ' + str(x2))

if D == 0:
    print('Корень будет единственный')
    x1 = - b - (2 * a)
    print('x1 = ' + str(x1))

if D < 0:
    print('Действительных корней нет')