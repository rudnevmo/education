while True:
    n = int(input('Введите факториал числа: '))
    fact = 1
    for i in range(2, n+1):
        fact = fact * i
    print('Факториал', n, 'это ', fact)