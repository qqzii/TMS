def my_fn1(fn1):
    def ff(words):
        x = fn1(words)
        return x.capitalize()
    return ff

@my_fn1
def swap_words(words):
    tmp = words.split(' ')
    return tmp[1] + ' ' + tmp[0]

# print(swap_words('привет мир'))

def my_fn2(fn2):
    def ff(ls):
        x = fn2(fn2(ls))
        return x
    return ff

@my_fn2
def mult_on_2(ls):
    result = []
    for x in ls:
        result.append(x * 2)
    return result

print(mult_on_2([1, 2, 3]))

import math

def my_fn3(fn3):
    def ff(x):
        if x < 0:
            print('Нельзя передавать отрицательные числа...')
            y = -1
        else:
            y = fn3(x)
        return y
    return ff

@my_fn3
def my_sqrt(x):
    return math.sqrt(x)

print(my_sqrt(3))
