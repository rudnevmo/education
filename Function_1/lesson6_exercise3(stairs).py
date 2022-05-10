def stairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return stairs(n - 1) + stairs(n - 2)

q = int(input('Введите кол-во ступеней: '))
print(stairs(q + 1))
