# Функция возвращает список, возвращает сумму значений и среднее значене, сортировка
def numb ():
    empty_list = []
    list_sorted = []
    for x in range(a):
        b = int(input('Enter numbers: '))
        empty_list.append(b)
    print(empty_list)
    print(sum(empty_list))
    print(round(sum(empty_list)/a))
    print(max(empty_list), ', ', min(empty_list))
    list_1 = empty_list.copy()
    empty_list.sort()
    print(empty_list)
    print(sorted(empty_list))
    print(list_1)

a = int(input('Enter amount of numbers: '))
numb ()