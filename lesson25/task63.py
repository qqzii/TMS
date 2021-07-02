# мутабельные

x1 = [1, 2, 3, True, 5.45, 'lol']

def f1(y):
    y[1] = 333
    y[3] = False
    y[4] = 5.99
    y[5] = 'ne lol'

# print(x1)
# f1(x1)
# print(x1)


# иммутабельные

x2int = 2
x2str = 'lol'

def f2int(y):
    y = 333
def f2str(y):
    y[0] = 'e'

# print(x2int)
# f2int(x2int)
# print(x2int)

# print(x2str)
# f2str(x2str)
# print(x2str)
