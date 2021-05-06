def f1(*args):
    return sum(args)

x1 = (1, 2, 3, 4, 5, 6)
# print(f1(*x1))

def f2(**kwargs):
    mult = 1
    for x in kwargs.values():
        mult *= x
    return mult

x2 = {'a':1, 'b':22, 'c':3}
# print(f2(**x2))

def f3(*args, **kwargs):
    sum1 = 0
    sum2 = 0
    for v in kwargs.values():
        sum1 += v
    for z in args:
        sum2 += z
    return sum1 + sum2

x3_1 = (1, 2)
x3_2 = {'a':1, 'b':2, 'c':3}
# print(f3(*x3_1, **x3_2))

def f4(*args, **kwargs):
    mult1 = 1
    mult2 = 1
    for v in args:
        mult1 *= v
    for z in kwargs.values():
        mult2 *= z
    return mult1 * mult2

x4_1 = (3, 2, 5)
x4_2 = {'x':2, 'y':5}
# print(f4(*x4_1, **x4_2))

def f5(*args, **kwargs):
    sum1 = 0
    sum2 = 0
    for v in kwargs.values():
        sum1 += v
    for z in args:
        sum1 += z
    return sum1 + sum2

x5_1 = (1, 2, 3)
x5_2 = {'a':1, 'b':4, 'c':7}
# print(f5(*x5_1, **x5_2))
