def f1():
    count = 10
    ls1 = []
    while count <= 20:
        ls1.append(count*count)
        count += 1
    return ls1

# print(f1())

def f2():
    count = 35
    ls2 = []
    while count <= 87:
        if count % 7 == 1 or count % 7 == 2 or count % 7 == 5:
            ls2.append(count)
        count += 1
    return ls2

# print(f2())

def f3():
    n = int(input('Введите число: '))
    sum = 0
    while n != 0:
        sum += n
        n -= 1
    return sum

# print(f3())

def f4(n):
    x1 = int(n / 100)
    x2 = int((n % 100) / 10)
    x3 = n % 10
    return x1 * x2 * x3

# print(f4(425))

def f5(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            count += 1
        n -= 1
    return count

# print(f5(109))

def f6(n):
    x1 = int(n / 100)
    x2 = int((n % 100) / 10)
    x3 = n % 10
    return max(x1, x2, x3)

# print(f6(683))

def f7(ls):
    new_ls = []
    for x in ls:
        x1 = int(x / 1000)
        x2 = int((x % 1000) / 100)
        x3 = int((x % 100) / 10)
        x4 = x % 10
        if x1 + x2 + x3 + x4 == 15:
            new_ls.append(x)
    return new_ls

# print(f7([1234, 2421, 5550, 5055, 1905, 3222, 1247, 9999, 4124, 1059]))
