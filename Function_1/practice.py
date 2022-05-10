#def rest_ethanol(total_mass, warehouse):
 #   ethanol = total_mass * 83 / 100
  #  warehouse -= ethanol # return возвращает 917 грам для следущего цикла
   # print('Остаток этанола на складе:', warehouse)
    #return warehouse #917 г


#warehouse = 1000
#mass = int(input('Масса готового антисептика (г): '))
#warehouse = rest_ethanol(mass, warehouse)
#mass = int(input('Масса готового антисептика (г): '))
#rest_ethanol(mass, warehouse)

#print()

#def function(a, b):
 #   if a == b:
  #      return b
   # return b + function(a, b - 1)

#number1 = int(input('Enter the first number: '))
#number2 = int(input('Enter the second number: '))
#print(function(number1, number2))

#print()

def multiply(c, d):
    if d == c: # рекурсия движется от большего к меньшему
        return d
    else:
        return d * multiply(c, d - 1) # d с каждым шагом уменьшается на -1 пока не станет равно с (4 * 3 *2 )
    # в конце, после последнего -1 d стало равно 2, равно с

number3 = int(input('Enter the third number: '))
number4 = int(input('Enter the fourth number: '))
print(multiply(number3, number4))

#print()

def even(e,f):
    while True:
        if f == e:
            return f
        elif f % 2 == 0:
            return f + even(e, f -1)
        else:
            f -= 1

num1 = int(input('Enter the fiveth number: '))
num2 = int(input('Enter the sixth number: '))
print(even(num1,num2))
