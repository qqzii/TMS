import random

def fn2(ls, a):
    raise Exception('Чужая функция')

def fn1(a):
    ls = []
    for i in range(100):
        ls.append(random.randint(1, 10000))
    fn2(ls, a)
    return 'OK'
