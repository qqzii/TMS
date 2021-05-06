def f11_2(x, y):
    sum = 0
    count = 0
    while count < y:
        sum += x
        count += 1
    return sum

# print(f11_2(2, 11))

def f12(x, y):
    mult = 1
    count = 0
    while count < y:
        mult *= x
        count += 1
    return mult

# print(f12(2, 9))

def f13():
    count1 = 0
    while count1 < 10:
        count2 = 0
        while count2 < 10:
            print(str(count1+1) + ' * ' + str(count2+1) + ' = ' + str((count1 + 1) * (count2 + 1)))
            count2 += 1
        count1 += 1
# f13()

def f17(x):
    count = 0
    while count < x:
        print('a   ' * x)
        count += 1

# f17(10)

def f18(x):
    count = 0
    while count < x:
        if (count < 1) or (count >= x - 1):
            print(' * ' * x)
        else:
            print(' * ' + '   ' * (x - 2) + ' * ')
        count += 1

# f18(6)

def f19(x):
    count = 0
    while count < x:
        if (count+1) % 2 != 0:
            print(' #    ' * int(x/2))
        else:
            print('    # ' * int(x/2))
        count += 1

# f19(10)

def f21(x):
    fact = 1
    count = 0
    while count < x:
        fact *= (count + 1)
        count += 1
    print(fact)

# f21(7)

def f22(sum, time, persent):
    count = 0
    while count < time:
        divident = (sum * (1 + persent / 100)) - sum
        sum += divident
        count += 1
    return sum

# sum_in = int(input('Введите вашу сумму: '))
# time_in = int(input('Введите время вклада: '))
# persent_in = int(input('Введите процент вклада: '))
#
# print(f22(sum_in, time_in, persent_in))

def f24(x):
    count = 0
    while count < x:
        print(' * ' * (count + 1))
        count += 1

# f24(6)

def f25(x):
    count = 0
    while count < x:
        kol_zn1 = 2*count+1
        kol_pr1 = int((x-1)/2-count)
        kol_zn2 = -(2*count) + (x*2-1)
        kol_pr2 = int(count-(x-1)/2)
        if count <= (x-1)/2:
            print(('   ' * kol_pr1) + (' * ' * kol_zn1) + ('   ' * kol_pr1))
        else:
            print(('   ' * kol_pr2) + (' * ' * kol_zn2) + ('   ' * kol_pr2))
        count += 1

# f25(9)
