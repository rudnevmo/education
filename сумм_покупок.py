price = 0

while True:
    buy = input('Введите цену товара (или 0 для окончания): ')
    if buy == '0':
        break
    elif buy == str:
        print('Не верно введены данные')
    else:
        price += float(buy)

print('Ваша сумма покупок: ', price)