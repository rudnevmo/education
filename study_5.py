    # Площадь тапеции и периметр трапеции + длинна окружности и объем шара
while True:
    men = int(input('''Выберите пункт меню:\n1. Площадь трапеции\n2. Периметр равносторонней трапеции\n3. Периметр разносторонней трапеции\n4. Выход\n:'''))

if men == 1:
    print(123)
def area(a, b, h):
    return (a + b) / 2 * h

def perimeterqua(a, b, c):
        return b * 2 + a + c
def perimeter(a, b, c, d):
        return a + b + c + d


a = int(input('Введите длинну верхней грани: '))
b = int(input('Введите длинну правой грани: '))
c = int(input('Введите длинну нижней грани: '))
d = int(input('Введите длинну левой грани: '))
h = int(input('Введите высоту: '))

if b == d:
    print('Периметр равносторонней трапеции равен ', perimeterqua(a, b, c), 'см', sep='')
else:
    print('Периметр трапеции равен ', perimeter(a, b, c, d), 'см', sep='')
print('Площадь трапеции равен ', area(a, b, h), 'см', sep='')

