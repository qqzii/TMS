def f1(x, y=7):
    return x*y

# print(f1(1, 2))
# print(f1(2))

def f2(ls1, ls2=[3, 4, 5]):
    return sum(ls1)+sum(ls2)

# print(f2([1, 2, 3], [1, 2, 3]))
# print(f2([1, 2, 3]))

def f3(x, y=7, dct={'divisor':10, 'divider':3}):
    return (x + y)/dct['divisor']

print(f3(1, 2))
print(f3(1))