def function(a, b):
    if a == b:
        return b
    return b + function(a, b - 1)

number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
print(function(number1, number2))