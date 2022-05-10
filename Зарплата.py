timeV = int(input('Отработанные часы Виктора: '))
cashV = float(input('Почасовая ставка, грн: '))
summV = timeV * cashV
print(summV, 'грн')

timeK = int(input('Отработанные часы Кристины: '))
cashK = float(input('Почасовая ставка, грн: '))
summK = timeK * cashK
print(summK, 'грн')

timeG = int(input('Отработанные часы Гриши: '))
cashG = float(input('Почасовая ставка, грн: '))
summG = timeG * cashG
print(summG, 'грн')

month = summG + summV + summK
year = float(month * 12)

print('Выплаты в месяц: ', month, 'грн')
print('Выплаты за год составят: ', year, 'грн')