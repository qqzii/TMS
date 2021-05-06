def condition1(x):
    if isinstance(x, int):
        if x <= 34:
            print('artem')
        else:
            print('tanya')
    else:
        raise Exception('Я принимаю только числа')

# condition1(32)

def condition2(x1, x2):
    if isinstance(x1, int) and isinstance(x2, int):
        if x1 + x2 == 5:
            return (x1 + x2) / 2
        else:
            return x1 + x2
    else:
        raise Exception('Я принимаю только числа')

# print('Результат: ' + str(condition2(1, 2)))

def condition3(string):
    if isinstance(string, str):
        if len(string) < 5:
            print(string)
        else:
            print('Строка сильно большая, я устал')
    else:
        raise Exception('Я печатаю только строки')

# condition3('qw')

import random
def condition5(x1, x2):
    while True:
        try:
            answer = int(input(str(x) + ' * ' + str(y) + ' = '))
            break
        except ValueError:
            print('Вы ввели не число!')
    if x1 * x2 == answer:
        print('Верно')
    else:
        print('Неверно')

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = int(random.choice(list_numbers))
y = int(random.choice(list_numbers))
# condition5(x, y)

def condition8(name):
    if name == 'Вася' or name == 'Петя' or name == 'Толик':
        if name == 'Вася' or name == 'Петя':
            print('Привет братан')
        else:
            print('Поделись на нолик')

    else:
        raise Exception('Я тебя не знаю')

# condition8('Петя')

def f1(x):
    sum = 0
    for digit in x:
        try:
            sum += digit
        except TypeError:
            print('Просуммировал только числа')
            continue
    return sum

# print(f1([1, 2, 3, 4, 7, 10, 0.1, 1, 's']))

def f5(x):
    if x != []:
        sum = 0
        count = 0
        for el in x:
            sum += el
            count += 1
        return sum / count
    else:
        raise Exception('Не могу посчитать среднее для пустого списка')

# print(f5([]))

def f6(x):
    if x != []:
        max_poisk = x[0]
        for el in x:
            if el > max_poisk:
                max_poisk = el
        return max_poisk
    else:
        raise Exception('Пустой список')

# print(f6([]))

def f8(x):
    mass = []
    for el in x:
        try:
            if el % 2 == 0:
                mass.append(el)
        except TypeError:
            print('Пропустил не число')
            continue
    return mass

# print(f8([1, 2, 3, 4, 5, 6, 7,'ss', 8]))
