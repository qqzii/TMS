from datetime import datetime

def prostoe(x):
    count = 2
    b = True
    while count < x:
        if x % count == 0:
            b = False
        count += 1
    return b, x

def lazy_map(fn, ls):
    for x in ls:
        y = fn(x)
        if y[0]:
            if y[1] != 0 and y[1] != 1:
                yield y[1]

def generator(x):
    start_time = datetime.now()
    generator = lazy_map(prostoe, range(1000000))
    for i in range(x):
        print(next(generator))
    print('Время работы: ' + str((datetime.now() - start_time).total_seconds()) + ' сек')

generator(6)
