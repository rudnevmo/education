
def greetings(name='Max'):
    name1 = str(input('Enter your name: '))
    if not name1:
        print('Hello, Max!')
    else:
        print('Hello, ', name1, '!', sep='')


greetings()