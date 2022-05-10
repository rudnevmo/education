import math

r = int(input('Введите радиус круга в миллиметрах, что бы узнать его площадь: '))
S = math.pi * r ** 2
S2 = round(S, 2)
S3 = S2/100
Scm = round(S3, 2)
print('Площадь круга равняется '+ str(S2) + ' мм^2 или ' + str(Scm) + ' см^2')