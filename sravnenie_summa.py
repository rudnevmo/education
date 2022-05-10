while True:

    print('Число А должно быть меньше числа В')
    a = int(input('Введите число а: '))
    b = int(input('Введите число b: '))

    if a < b:
        i = a
        suma = 0
        while i <= b:
            suma += i
            i += 1
        print(suma)
    else:
        print('"В" долно быть больше, чем "А"')
        continue