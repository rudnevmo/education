def palin(string):
    string.replace(' ', '')
    revers_string = string[::-1]
    if string == revers_string:
        return 'Yes, palindrom'
    else:
        return 'No, not palindrom'

string = input('Введите фразу для проверки на палиндромизм: ')
print(palin(string))

