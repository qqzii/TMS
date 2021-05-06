def f1(x):
    sum = 0
    for digit in x:
        sum += digit
    return sum

# print(f1([1, 2, 3, 4, 5, 6]))

def f2(x):
    ls = []
    for digit in x:
        ls.append(digit / 2)
    return ls

# print(f2([1, 2, 3, 4, 5, 6]))

def f3(x):
    count = 0
    for el in x:
        count += 1
    return count

# print(f3([1, 2, 3, 4, 5, 6]))

def f4(x, y):
    answer = False
    for el in x:
        if el == y:
            answer = True
    return answer

# print(f4([1, 2, 3, 4, 5, 6], 5))

def f5(x):
    sum = 0
    count = 0
    for el in x:
        sum += el
        count += 1
    return sum / count

# print(f5([1, 2, 3, 4, 5, 6]))

def f6(x):
    if x == []:
        print('Строка пустая...')
    else:
        max_poisk = x[0]
        for el in x:
            if el > max_poisk:
                max_poisk = el
        return max_poisk

# print(f6([1, 2, 3, 4, 5]))

def f7(x):
    if x == []:
        print('Строка пустая...')
    else:
        min_poisk = x[0]
        for el in x:
            if el < min_poisk:
                min_poisk = el
        return min_poisk

# print(f7([1, 2, 3, 4, 5]))

def f8(x):
    mass = []
    for el in x:
        if el % 2 == 0:
            mass.append(el)
    return mass

# print(f8([1, 2, 3, 4, 5, 6, 7, 8]))

def f9(x):
    mass = []
    for el in x:
        if el % 2 != 0:
            mass.append(el)
    return mass

# print(f9([1, 2, 3, 4, 5, 6, 7, 8]))

def f10(x, y):
    mass = []
    for i in x:
        for j in y:
            if i == j:
                mass.append(i)
    return mass

# print(f10([1, 2, 3, 4, 5, 6, 7, 8], [11, 12, 14, 15, 8, 1]))

def f11(x, y):
    mass = []
    for i in x:
        for j in y:
            if i != j:
                continue
            else:
                mass.append(j)
    return mass

# print(f11([1, 2, 3, 4, 5, 6, 7, 8], [12, 14, 15, 8, 1]))

def f11_2(x, y):
    sum = 0
    for i in range(x):
        sum += y
    return sum

# print(f11_2(3, 10))

def f12(x, y):
    mult = 1
    for i in range(y):
        mult *= x
    return mult

# print(f12(4, 3))

def f13():
    for i in range(10):
        for j in range(10):
            print(str(i+1) + ' * ' + str(j+1) + ' = ' + str((i + 1) * (j + 1)))

# f13()

def f14(x):
    print('   ' + str(x[0]))
    x1 = len(str(x[0]))
    for digit in x[1:]:
        y = len(str(digit))
        print((3 + x1 - y) * ' ' + str(digit))

# f14([10000, 122, 34, 24, 4125, 4446, 71, 8])

import random
def f15():
    answer = 1
    count = 0
    list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    while int(answer) != -1:
        x = int(random.choice(list_numbers))
        y = int(random.choice(list_numbers))
        answer = input(str(x) + ' * ' + str(y) + ' = ')
        if int(answer) == (x * y):
            count += 1
        else:
            if int(answer) == -1:
                print('Ваш конечный счет: ' + str(count))
                continue
            else:
                count -= 1
        print('Ваш текущий счет: ' + str(count))

#f15()

def f16(x):
    if x == []:
        print('Строка пустая...')
    else:
        max_search = x[0]
        mass2 = []
        for el in x:
            if el > max_search:
                max_search = el
        for el in x:
            if el != max_search:
                mass2.append(el)
        max2_search = mass2[0]
        for el2 in mass2:
            if el2 > max2_search:
                max2_search = el2
        return max_search, max2_search
# print(f16([1, 2, 3, 4, 5]))

def f17(x):
    for digit in range(x):
        print('a   ' * x)

# f17(10)

def f18(x):
    for i in range(x):
        if (i < 1) or (i >= x - 1):
            print(' * ' * x)
        else:
            print(' * ' + '   ' * (x - 2) + ' * ')

# f18(6)

def f19(x):
    for i in range(x):
        if (i+1) % 2 != 0:
            print(' #    ' * int(x/2))
        else:
            print('    # ' * int(x/2))
# f19(10)

def f20(x, y):
    ls = []
    for i in range(y - x - 1):
        if (x + 1) % 2 == 0:
            ls.append(x + 1)
            x += 1
        else:
            x += 1
    print(ls)

# f20(6, 21)

def f21(x):
    fact = 1
    for i in range(x):
        fact *= (i + 1)
    print(fact)

# f21(10)

def f22(sum, time, persent):
    for i in range(time):
        divident = (sum * (1 + persent / 100)) - sum
        sum += divident
    return sum

# sum_in = int(input('Введите вашу сумму: '))
# time_in = int(input('Введите время вклада: '))
# persent_in = int(input('Введите процент вклада: '))

# print(f22(sum_in, time_in, persent_in))

def f23(x):
    ind = True
    for i in range(x):
        if i == 0 or i == 1 or i == x:
            continue
        else:
            if x / i == int(x / i):
                ind = False
    return ind

# digit23 = int(input('Введите число для проверки: '))
# print(f23(digit23))

def f24(x):
    for i in range(x):
        print(' * ' * (i + 1))

# f24(10)

def f25(x):
    for i in range(x):
        kol_zn1 = 2*i+1
        kol_pr1 = int((x-1)/2-i)
        kol_zn2 = -(2*i) + (x*2-1)
        kol_pr2 = int(i-(x-1)/2)
        if i <= (x-1)/2:
            print(('   ' * kol_pr1) + (' * ' * kol_zn1) + ('   ' * kol_pr1))
        else:
            print(('   ' * kol_pr2) + (' * ' * kol_zn2) + ('   ' * kol_pr2))

# f25(11)

def f26(date1, date2):
    mass1 = date1.split('/')
    day1 = int(mass1[0])
    month1 = int(mass1[1])
    year1 = int(mass1[2])
    mass2 = date2.split('/')
    day2 = int(mass2[0])
    month2 = int(mass2[1])
    year2 = int(mass2[2])
    error = False
    if (month1 or month2) > 12 or (month1 or month2) <= 0:
        error = True
    if (day1 or day2) <= 0:
        error = True
    if (month1 or month2) == (1 or 3 or 5 or 7 or 8 or 10 or 12):
        if (day1 or day2) > 31:
            error = True
    else:
        if (month1 or month2) != 2:
            if (day1 or day2) > 30:
                error = True
        else:
            if (year1 or year2) % 4 == 0:
                if (day1 or day2) > 29:
                    error = True
            else:
                if (day1 or day2) > 28:
                    error = True
    if error == True:
        print('Ввод некорректен...')
    else:
        count_v_years1 = 0
        count_v_years2 = 0
        for i in range(year1-1):
            if i % 4 == 0:
                count_v_years1 += 1
        for i in range(year2-1):
            if i % 4 == 0:
                count_v_years2 += 1
        days_in_year1 = (year1 - count_v_years1) * 365 + count_v_years1 * 366
        days_in_year2 = (year2 - count_v_years2) * 365 + count_v_years2 * 366
        days_in_month1 = 0
        days_in_month2 = 0
        for i in range(month1-1):
            if i == 1 or 3 or 5 or 7 or 8 or 10 or 12:
                days_in_month1 += 31
            else:
                if i != 2:
                    days_in_month1 += 30
                else:
                    if year1 % 4 == 0:
                        days_in_month1 += 29
                    else:
                        days_in_month1 += 28
        for j in range(month2-1):
            if j == 1 or 3 or 5 or 7 or 8 or 10 or 12:
                days_in_month2 += 31
            else:
                if j != 2:
                    days_in_month2 += 30
                else:
                    if year2 % 4 == 0:
                        days_in_month2 += 29
                    else:
                        days_in_month2 += 28
        total_difference = abs((days_in_year1 + days_in_month1 + day1) - (days_in_year2 + days_in_month2 + day2))
        print('Разница между введенными датами: ' + str(total_difference))

# input_date1 = input('Введи первую дату через / : ')
# input_date2 = input('Введи вторую дату через / : ')
# f26(input_date1, input_date2)
