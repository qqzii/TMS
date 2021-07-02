def f1(ls):
    _, (x, _), y = ls
    return x, y

print(f1([4, [7, 8], 6]))


def f2(ls):
    sum = 0
    for (_, (x, _)) in ls:
        sum += x
    return sum

print(f2([(3, [9, 1]), [(23, 43), [5, 4]]]))
