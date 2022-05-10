while True:

    action = input('Menu\n1.Addition (+)\n2.Subtraction (-)\n3.Division (/)\n4.Multipliction (*)\n5.Exit\n> ')
    if action == '5':
        print('You exit')
        break
    else:
        print('Select functin!')
        print()
        continue

    a = float(input('Enter the first number: '))
    b = float(input('Enter the second number: '))

    def addition(a, b):
        return a + b

    def subtraction(a, b):
        return a - b

    def division(a, b):
        return a / b

    def multipliction(a, b):
        return a * b

    if action == '1':
        print('Результат сложения: ', addition(a, b))
    elif action == '2':
        print('Результат вычитаня: ', subtraction(a, b))
    elif action == '3':
        if b == 0:
            print("Can't divide by zero!")
            print()
            continue
        print('Результат деления: ', division(a, b))
    elif action == '4':
        print('Результат умножения: ', multipliction(a, b))
    else:
        print('Select functin!')

    print()