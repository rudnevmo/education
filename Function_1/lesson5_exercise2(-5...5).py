def alg(x):
    if x < 0:
       return x * 2
    else:
        return x * 3
    print(x)

def step():
    y = -5
    while y < 5:
        y += 0.5
        z = alg(y)
        print('Function (', y, ')\t =\t', z)

step()


