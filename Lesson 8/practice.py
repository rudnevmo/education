# работа со списками. Напсать функцию, котораяна вход будет принимаь 2 списка и возвращать саисок с уникальными значениями

def qva(a2, b2):
    list3 = []
    list4 = []
    for i in a2:
        if i not in b2:
            list3.append(i)
    for j in b2:
        if j not in a2:
            list3.append(j)
    for k in list3:
        if k not in list4:
            list4.append(k)
    return list4


a = input('Enter first numbers: ')
b = input('Enter second numbers: ')
a1 = a.split()
b1 = b.split()
a2 = list(map(int, a1))
b2 = list(map(int, b1))

print(qva(a2, b2))