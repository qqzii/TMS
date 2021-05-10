def f1():
    count = 10
    ls1 = []
    while count <= 20:
        ls1.append(count*count)
        count += 1
    return ls1

# print(f1())

def f2():
    count = 35
    ls2 = []
    while count <= 87:
        if count % 7 == 1 or count % 7 == 2 or count % 7 == 5:
            ls2.append(count)
        count += 1
    return ls2

# print(f2())

def f3():
    n = int(input('Введите число: '))
    sum = 0
    while n != 0:
        sum += n
        n -= 1
    return sum

# print(f3())

def f4(n):
    x1 = int(n / 100)
    x2 = int((n % 100) / 10)
    x3 = n % 10
    return x1 * x2 * x3

# print(f4(425))

def f5(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            count += 1
        n -= 1
    return count

# print(f5(109))

def f6(n):
    x1 = int(n / 100)
    x2 = int((n % 100) / 10)
    x3 = n % 10
    return max(x1, x2, x3)

# print(f6(683))

def f7(ls):
    new_ls = []
    for x in ls:
        x1 = int(x / 1000)
        x2 = int((x % 1000) / 100)
        x3 = int((x % 100) / 10)
        x4 = x % 10
        if x1 + x2 + x3 + x4 == 15:
            new_ls.append(x)
    return new_ls

# print(f7([1234, 2421, 5550, 5055, 1905, 3222, 1247, 9999, 4124, 1059]))

def f8(x):
    count = 2
    b = True
    while count < x:
        if x % count == 0:
            b = False
        count += 1
    return b

# print(f8(809))

def f9(x):
    count = 2
    ls = []
    while count < x:
        if x % count == 0:
            ls.append(count)
        count += 1
    return ls

# print(f9(15))

def f10(a, n):
    power = a
    while n > 1:
        power *= a
        n -= 1
    return power

# print(f10(2, 6))

def f11(ls):
    count = 0
    for x in ls:
        if max(ls) == x:
            count += 1
    return max(ls), count

# print(f11([1, 2, 3, 4, 51, 101, 101, 100, 101, 2, 66]))

import math
def f12():
    radius = int(input('Введите радиус круга: '))
    quantity = int(input('Введите количество точек: '))
    count = 0
    ls = []
    ls_answer = []
    while count < quantity:
        xy_dot = input('Введите координаты точки ' + str(count + 1) + ' x,y: ')
        coo = xy_dot.split(',')
        s = math.sqrt(int(coo[0])**2 + int(coo[1])**2)
        if s > radius:
            ls.append(s)
            ls_answer.append((coo[0], coo[1]))
        count += 1
    count = 0
    for x in ls:
        if x == min(ls):
            return ls_answer[count]
        count += 1

# print(f12())

def f13():
    x = int(input('Введите координату проверяемой точки: '))
    quantity = int(input('Введите количество отрезков: '))
    count = 0
    count1 = 0
    while count < quantity:
        xy_dot = input('Введите координаты отрезка ' + str(count + 1) + ' xmin, xmax: ')
        xmin, xmax = xy_dot.split(',')
        if (x > int(xmin)) and (x < int(xmax)):
            count1 += 1
        count += 1
    if count1 == quantity:
        return True
    else:
        return False

# print(f13())

def f15():
    quantity = 0
    while quantity < 3:
        quantity = int(input('Введите количество сторон(>3): '))
    count = 0
    ls = []
    while count < quantity:
        ls.append(int(input('Введите количество плит на стороне ' + str(count + 1) + ': ')))
        count += 1
    if sum(ls) % 2 == 0:
        return int(sum(ls) / 2)
    else:
        return int(int(sum(ls) / 2) + 1)

# print(f15())

def f16():
    min = int(input('Введите число минут: '))
    hours_enter = int(input('Введите число часов: '))
    hours = hours_enter * 5 + int(min / 12)
    count = 0
    while min != hours:
        min += 12
        hours += 1
        count += 12
        if min > 60:
            min %= 60
        if hours > 60:
            hours %= 60
    return count

# print(f16())

# def f17():
