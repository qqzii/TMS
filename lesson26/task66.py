import math
from functools import partial

def f1(x, y):
    z = math.sqrt(x**2 + y**2)
    return z

def experiment():
    f2 = partial(f1, 3)
    print(f2)
    print(f2(4))

experiment()
