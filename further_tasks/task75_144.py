import math

def f75():
    print('You are welcome!\n' * 10)

# f75()

def f76():
    x = int(input('Сколько раз выводить: '))
    print('Silence is golden\n' * x)

# f76()

def f77():
    x = int(input('Количество строк: '))
    print('0 0 0 0 0\n' * x)

# f77()

def f78(quantity):
    print((' * ' * quantity + '\n') * quantity)

# f78(3)

def f79():
    count = 0
    while count < 20:
        if count == 19:
            print(str(count + 1))
        else:
            print(str(count + 1) + ', ', end='')
        count += 1

# f79()

def f80():
    count = 1000
    while count < 1025:
        if count == 1024:
            print(str(count + 1))
        else:
            print(str(count + 1) + ', ', end='')
        count += 3

# f80()

def f81():
    count = 100
    while count >= 0:
        if count == 0:
            print(str(count))
        else:
            print(str(count) + ', ', end='')
        count -= 4

# f81()

def f82():
    count = 12
    while count < 29:
        if count == 28:
            print(str(count/10))
        else:
            print(str(count/10) + ', ', end='')
        count += 2

# f82()

def f83():
    ls = [25, 25.5, 24.8]
    count = ls[0]
    while count < 36:
        for i in ls:
            print(str(i) + '  ', end='')
        print()
        score = 0
        while score < len(ls):
            ls[score] += 1
            score += 1
        count += 1
# f83()

def f84():
    count = 1
    while count <= 100:
        print(str(count) + '$  -  ' + str(count * 74) + 'р  -  ' + str("%.1f" % (count * 3.7)) + 'кг')
        count += 1

# f84()

def f85():
    name = input('Введите название: ')
    site = input('Введите ссылку на веб-сайт: ')
    if len(name) > 26 and len(site) > 26:
        print('Слишком длиный ввод')
    else:
        count = 0
        while count < 18:
            if (count == 0) or (count == 17):
                print('[' * 15 + ' ' * 10 + ']' * 15)
            if (count == 1) or (count == 2) or (count == 15) or (count == 16):
                print('[' + ':' * 14 + ' ' * 10 + ':' * 14 + ']')
            if (count == 3) or (count == 14):
                print('[' + ':' * 6 + '[' * 7 + ':' + ' ' * 10 + ':' + ']' * 7 + ':' * 6 + ']')
            if ((count > 3) and (count < 8)) or ((count > 9) and (count < 14)):
                print('[' + ':' * 5 + '[' + ' ' * 26 + ']' + ':' * 5 + ']')
            if count == 8:
                if len(name) % 2 == 0:
                    print('[' + ':' * 5 + '[' + ' ' * int((26 - len(name)) / 2) + name + ' ' * int((26 - len(name)) / 2) + ']' + ':' * 5 + ']')
                else:
                    print('[' + ':' * 5 + '[' + ' ' * (int((26 - len(name)) / 2) + 1) + name + ' ' * int((26 - len(name)) / 2) + ']' + ':' * 5 + ']')
            if count == 9:
                if len(site) % 2 == 0:
                    print('[' + ':' * 5 + '[' + ' ' * int((26 - len(site)) / 2) + site + ' ' * int((26 - len(site)) / 2) + ']' + ':' * 5 + ']')
                else:
                    print('[' + ':' * 5 + '[' + ' ' * (int((26 - len(site)) / 2) + 1) + site + ' ' * int((26 - len(site)) / 2) + ']' + ':' * 5 + ']')
            count += 1

# f85()

def f86():
    n = int(input('Введите число: '))
    sum = 0
    while n > 0:
        sum += n
        n -= 1
    print(sum)

# f86()

def f87():
    n = 88
    sum = 0
    while n > 9:
        sum += n
        n -= 1
    print(sum)

# f87()

def f88():
    n = 13
    fact = 1
    while n > 4:
        fact *= n
        n -= 1
    print(fact)

# f88()

def f89():
    n = 112
    sum = 0
    while n > 0:
        sum += n
        n -= 3
    print(sum)

# f89()

def f90():
    n = 111
    sum = 0
    while n > 2:
        sum += math.cos(n / (n + 2))
        n -= 2
    print(sum)

# f90()

def f91():
    n = 9
    sum = 0
    while n > 1:
        sum += n / (n + 1)
        n -= 1
    print(sum)

# f91()

def f92():
    n = 1
    sum = 0
    while n < 101:
        sum += n
        print(sum)
        n += 1

# f92()

def f93():
    n = int(input('Введите число: '))
    sum = 0
    while n > 0:
        sum += n**2
        n -= 1
    print(sum)

# f93()

def f94():
    n = int(input('Введите число: '))
    sum = 0
    while n > 0:
        sum += 1 / n
        n -= 1
    print(sum)

# f94()

def f95():
    a = int(input('Введите a: '))
    n = int(input('Введите n: '))
    p = 1
    while n > 0:
        p *= (a + n)**2
        n -= 1
    print(p)

# f95()

def f96():
    x = int(input('Введите x: '))
    n = int(input('Введите n: '))
    sum = 0
    while n > 0:
        sum += 1 / (math.cos(x))**n
        n -= 1
    print(sum)

# f96()

def f97():
    n = int(input('Введите n: '))
    count = 1
    sum = 0
    while count <= n:
        sum += int(math.factorial(count * 2) / math.factorial(count - 1))
        count += 1
    print(sum)

# f97()

def f98():
    c = int(input('Введите число тренировок: '))
    x = 10
    sum = 0
    n = 1
    print('\na)')
    while n <= 10:
        print(str(n) + '  ' + str(x))
        if n <= 7:
            sum += x
        x += x*0.1
        n += 1
    print('\nб)')
    print(sum)
    x = 10
    sum = 0
    n = 1
    while n <= c:
        sum += x
        x += x * 0.1
        n += 1
    x = 10
    count = 1
    while x < 80:
        x += x * 0.1
        count += 1
    print('\nв)')
    print(sum)
    print('\nг)')
    print(count)

# f98()

def f99():
    n = 1000
    while n <= 9999:
        thousand = int(n/1000)
        hundreds = (int(n/100)) - thousand * 10
        units = int(n % 10)
        dozens = int((int(n % 100) - units) / 10)
        first_if = (thousand != hundreds) and (thousand != dozens) and (thousand != units)
        second_if = (hundreds != dozens) and (hundreds != units)
        third_if = (dozens != units)
        if first_if and second_if and third_if:
            print(n)
        n += 1

# f99()

def f100():
    n = 1000
    while n <= 9999:
        thousand = int(n/1000)
        hundreds = (int(n/100)) - thousand * 10
        units = int(n % 10)
        dozens = int((int(n % 100) - units) / 10)
        first_if = thousand != 5 and thousand != 6
        second_if = hundreds != 5 and hundreds != 6
        third_if = dozens != 5 and dozens != 6
        four_if = units != 5 and units != 6
        if first_if and second_if and third_if and four_if:
            print(n)
        n += 1

# f100()

def f101():
    n = 10000
    while n <= 99999:
        tens_of_thousand = int(n / 10000)
        thousand = int(n / 1000) - tens_of_thousand * 10
        hundreds = int(n / 100) - (tens_of_thousand * 100 + thousand * 10)
        units = int(n % 10)
        dozens = int((int(n % 100) - units) / 10)
        first_if = n % 2 == 0
        second_if = hundreds % 2 == 1
        third_if = (tens_of_thousand + thousand + hundreds + dozens + units) % 4 == 0
        if first_if and second_if and third_if:
            print(n)
        n += 1

# f101()

def f102():
    n = 1000
    while n <= 9999:
        thousand = int(n/1000)
        hundreds = (int(n/100)) - thousand * 10
        units = int(n % 10)
        dozens = int((int(n % 100) - units) / 10)
        if thousand == 3 or hundreds == 3 or dozens == 3 or units == 3:
            print(n)
        n += 1

# f102()

def f103():
    n = 100
    while n <= 999:
        hundreds = int(n/100)
        units = int(n % 10)
        dozens = int((int(n % 100) - units) / 10)
        if n == (hundreds**3 + dozens**3 + units**3):
            print(n)
        n += 1

# f103()

def f104():
    n = 1000
    count = 0
    while n <= 9999:
        thousand = int(n/1000)
        hundreds = (int(n/100)) - thousand * 10
        units = int(n % 10)
        dozens = int((int(n % 100) - units) / 10)
        if n == 600 * (thousand + hundreds + dozens + units):
            print(n)
            count += 1
        n += 1
    print('Ответ: ' + str(count))

# f104()

def f105():
    n = 0
    condition = True
    while condition:
        if n % 11 == 0 and n % 2 == 1 and n % 3 == 1 and n % 4 == 1 and n % 5 == 1 and n % 6 == 1 and n % 7 == 1 and n % 8 == 1 and n % 9 == 1 and n % 10 == 1:
            print(n)
            condition = False
        n += 1

# f105()

def f106():
    n = int(input('Введите n: '))
    print('1' * n)
    print('2' * (2*n))
    print('3' * (3*n))

# f106()

def f107():
    n = 10
    sum = 0
    while n > 0:
        print((str(n) + ' ') * n)
        sum += n * n
        n -= 1
    print(sum)

# f107()

def f108():
    n = int(input('Введите n: '))
    count = 1
    while count <= n:
        print(' * ' * count)
        count += 1

# f108()

def f109():
    n = int(input('Введите n: '))
    count = 1
    while count <= n:
        if count % 2 == 1:
            print(' * ' * 7)
        else:
            print(' * ' * 4)
        count += 1

# f109()

def f110():
    n = int(input('Введите n: '))
    m = int(input('Введите m: '))
    count = 1
    while count <= n:
        print((' A ' * 3 + ' B ' * 3) * m)
        count += 1

# f110()

def f111():
    n = int(input('Введите n: '))
    count = 1
    while count <= n:
        if count == 1 or count == n:
            print(' A ' * (2 * n))
        else:
            print(' A ' + ' B ' * (2 * n - 2) + ' A ')
        count += 1

# f111()

def f112():
    n = 10
    while n > 0:
        count = 10
        while count > 0:
            if count == n:
                print(' 0 ', end='')
            else:
                print(' 1 ', end='')
            count -= 1
        print(end='\n')
        n -= 1

# f112()

def f113():
    count = 1
    while count <= 20:
        if count % 2 == 0:
            print(str(count) * 10)
        else:
            print('1' * 10)
        count += 1

# f113()
