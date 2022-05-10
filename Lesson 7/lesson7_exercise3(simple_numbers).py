def multip(e, d):
    if d == e:
        return d
    else:
        return d * multip(e, d - 1)
couten = []
a = int(input('Enter start of list: '))
b = int(input('Enret finih of list: '))
lis = []
for i in range(a, b + 1):
    for j in range(a, i):
        if i % j == 0:
            break
    else:
        lis.append(i)
print()
print('Simple numbers: ', lis)
c = int(input('Select function:\n1.Sum\n2.Multiplication\n> '))
if c == 1:
    print()
    print('Sum of list: ', sum(lis))
elif c == 2:
    print()
    print('Multiplication of list: ', multip(lis[0], lis[-1]))
