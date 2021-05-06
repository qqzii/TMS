def f1(x, y):
    return x + y
print(f1(1, 44))

def f2(x):
    return x * 4
print(f2(1))

def f3(x, y, z):
    return (x + y + z) / 3
print(f3(3, 44, 22))

def f4():
    return 7
print(f4())

def f5(x):
    return x % 5
print(f5(22))

def f6(x, y):
    return {'first': x, 'second': y, 'sum': x + y}
print(f6(77, 4))

def f7(x):
    return (4 in x) or (8 in x)
print(f7([2, 3, 5, 6, 7, 8, 4]))

def f8(x, y):
    return x[1] / y[0]
print(f8([1, 22], [2, 11]))

def f9(x):
    return x.replace(' ', 'privet')
print(f9('1 2 3 4 5'))

def f10(x):
    return x.split(' ')[1]
print(f10('записаться на курсы можно завтра в десять утра'))

def f11(x):
    x[1] = 4
    return x
print(f11([1, 2, 3, 44, 5]))

def f12(x):
    x['a'] = 86
    return x
print(f12({'a': 2, 'b': 22, 'c': 11}))

def f13(x):
    del x['b']
    return x
print(f13({'a': 2, 'b': 22, 'c': 11}))

def f14(x):
    x[2] += 33
    return x
print(f14([11, 2, 3, 44, 61]))

def f15(x):
    sum = x[0] + x[-1]
    x.append(sum)
    return x
print(f15([11, 2, 3, 44, 61, 21, 66, 62]))

def f16(x):
    x['c'] = x['a'] + 45
    return x
print(f16({'a': 12, 'b': 111}))

def f17(x):
    x[1] = x[0]
    return x
print(f17([1, 2, 3, 4]))

def f18(x, y):
    del x['a']
    x['c'] = y
    return x
print(f18({'a': 12, 'b': 21}, 66))

def f19(x):
    y = [x[0], x[-1]]
    return y
print(f19([1, 2, 3, 4]))

def f20(x):
    y = [x['b'], x['m']]
    return y
print(f20({'a': 12, 'b': 44, 'm': 1, 'n': 0}))

def f21(x, y):
    null_list = []
    null_list.append(x)
    z = null_list + y
    return z
print(f21(11, [1, 2, 3, 4]))

def f22(x):
    return str(len(x.split(' '))) + ' - одиночных пробелов'
print(f22('привет меня зовут Артем'))

def f23(x):
    z = x.split(' ')
    b = z[0]
    z[0] = z[1]
    z[1] = b
    return ' '.join(z)
print(f23('привет друг'))
