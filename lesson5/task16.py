def funk1(x):
    if x > 100:
        return x * 2
    else:
        return x / 3

# print(list(map(funk1, [1, 2, 3, 4, 5, 200, 100, 222])))

def funk2(x):
    return x % 2 == 0

# print(list(filter(funk2, [1, 2, 3, 4, 5, 6])))

from functools import reduce
def funk3(x, y):
    return x + y

# print(reduce(funk3, [1, 2, 3, 4, 5, 6], 0))

def funk4(x):
    if x > 100:
        return x * 2
    else:
        return x / 3

def my_map(funk, ls):
    new_ls = []
    for q in ls:
        new_ls.append(funk(q))
    return new_ls

# print(my_map(funk4, [1, 2, 3, 4, 5, 200, 100, 222]))

def funk5(x):
    return x % 2 == 0

def my_filter(funk, ls):
    new_ls = []
    for q in ls:
        if funk(q):
            new_ls.append(q)
    return new_ls

# print(my_filter(funk5, [1, 2, 3, 4, 5, 6]))

def funk6(x):
    return x - 2

def my_funk(funk, x, z):
    count = 0
    while count < z:
        x = funk(x)
        count += 1
    return x

# print(my_funk(funk6, 20, 3))

def funk7(x, y):
    if x > y:
        return x
    else:
        return y
print(reduce(funk7, [11, 111, 1, 2, 3, 4, 5, 6],))

def funk8(x, y):
    return x * y

def my_reduce(funk, x, y):
    count = 0
    while count < len(x):
        y = funk(x[count], y)
        count += 1
    return y

# print(my_reduce(funk8, [2, 3, 4], 2))
