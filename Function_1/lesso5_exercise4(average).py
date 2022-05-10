while True:
    choo = input('1.Average\n2.Exit\n> ')

    def avera(a, b, c):
        return (a + b + c) / 3
        print('The average for ', a, b, c, 'equals ', agerage(a, b, c))

    if choo == '1':
        a = float(input('Enter first number: '))
        b = float(input('Enter second number: '))
        c = float(input('Enter third number: '))
        print('The average for ', a, b, c, 'equals ', avera(a, b, c))
        print()
    else:
        print('You exit')
        break
