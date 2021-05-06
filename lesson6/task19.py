def f1(*args):
    return sum(args)
# print(f1(1, 2, 3, 4, 5, 6))

def f2(**kwargs):
    mult = 1
    for x in kwargs.values():
        mult *= x
    return mult

# print(f2(a=1, b=22, c=3))

def f3(x, y, **kwargs):
    sum = 0
    for v in kwargs.values():
        sum += v
    return x + y + sum

# print(f3(1, 2, a=1, b= 2, c=3))

def f4(*args, x=2, y=5):
    mult = 1
    for v in args:
        mult *= v
    return x * y * mult

# print(f4(3, 2, 5))

def f5(*args, **kwargs):
    sum1 = 0
    sum2 = 0
    for v in kwargs.values():
        sum1 += v
    for z in args:
        sum1 += z
    return sum1 + sum2

# print(f5(1, 2, 3, a=1, b=4, c=7))
