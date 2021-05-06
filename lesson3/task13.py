def condition1(x, name1, name2):
    if x <= 34:
        print(name1)
    else:
        print(name2)

arg = int(input('Введите число: '))
my_name = input('Введите ваше имя: ')
mom_name = input('Введите имя вашей матери: ')
# condition1(arg, my_name, mom_name)

def condition2(x1, x2):
    if x1 + x2 == 5:
        return (x1 + x2) / 2
    else:
        return x1 + x2

arg1 = int(input('Введите первое число: '))
arg2 = int(input('Введите второе число: '))
# print('Результат: ' + str(condition2(arg1, arg2)))

def condition3(string):
    if len(string) < 5:
        print(string)
    else:
        print('Строка сильно большая, я устал')

arg = input('Введите строку: ')
# condition3(arg)

def condition4(x1, x2):
    if x1 > x2:
        return x1 + x2
    else:
        return x1 * x2

arg1 = int(input('Введите первое число: '))
arg2 = int(input('Введите второе число: '))
# print('Результат: ' + str(condition4(arg1, arg2)))

import random
def condition5(answer, x1, x2):
    if x1 * x2 == answer:
        print('Верно')
    else:
        print('Неверно')

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = int(random.choice(list_numbers))
y = int(random.choice(list_numbers))
arg = int(input(str(x) + ' * ' + str(y) + ' = '))
# condition5(arg, x, y)

def condition6(answer, dict):
    # такое лучше через switch конечно
    if dict[answer] == dict['c']:
        print('Верно, Минск - столица Беларуси')
    else:
        if dict[answer] == dict['b']:
            print('Лондон - столица Великобритании')
        else:
            print('Бобруйск - город в Беларуси, но не столица')

dict_cities = {'a': 'Бобруйск', 'b': 'Лондон', 'c':'Минск'}
print('Столица Беларуси:\na. ' + dict_cities['a'] + '\nb. ' + dict_cities['b'] + '\nc. ' + dict_cities['c'])
arg = input('Введите букву вашего ответа: ')
# condition6(arg, dict_cities)

def condition7(string, word1, word2):
    if word1 in string:
        print(string.replace(word1, word2))
    else:
        print('Слова, которое вы ввели нет в строке')

str1 = input('Введите строку: ')
str2 = input('Введите слово, которое заменить: ')
str3 = input('Введите слово, которым заменить: ')
# condition7(str1, str2, str3)

def condition8(name):
    # это тоже лучше через switch
    if name == 'Вася' or name == 'Петя':
        print('Привет братан')
    else:
        if name == 'Толик':
            print('Поделись на нолик')
        else:
            print('Я тебя не знаю...')

names = input('Введи свое имя: ')
# condition8(names)

def condition9(date):
    mass = date.split('/')
    day = int(mass[0])
    month = int(mass[1])
    year = int(mass[2])
    error = False
    position = ''
    if year >= 2021:
        if month >= 4:
            if day >= 12:
                position = 'FUTURE'
    if year < 0:
        position = 'BC'
    if month > 12 or month <= 0:
        error = True
    if day <= 0:
        error = True
    if month == (1 or 3 or 5 or 7 or 8 or 10 or 12):
        if day > 31:
            error = True
    else:
        if month != 2:
            if day > 30:
                error = True
        else:
            if year % 4 == 0:
                if day > 29:
                    error = True
            else:
                if day > 28:
                    error = True
    if error == True:
        print('Введена некорректная дата...')
    else:
        if position == 'BC':
            print('До нашей эры? Серьезно?')
        else:
            if position == 'FUTURE':
                print('Будущее?')
            else:
                print('Такая дата существует!')

input_date = input('Введи дату через / : ')
# condition9(input_date)
