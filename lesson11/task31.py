import random

# a = random.randint(1, 100)
# b = random.randint(1, 100)
# c = a + b
# x = random.randint(1, 100)
# z = x + b * c
# k = (random.randint(1, 100) + z) * 5
# print("k ravno " + str(k))
# for m in range(4):
#     k = k + m
# k = k / 12
# print("k ravno " + str(k))

# x = random.randint(1, 100)
# a = x + 18
# b = a * 2
# x = a + b
# d = int(x * 0.00021)
# y = -1 + (x ** d) + 1
# z = x / y
# z = z + 21
# print("Rezultat: " + str(z))

a = random.randint(1, 100)
b = random.randint(1, 100)
c = a + b
x = random.randint(1, 100)
z = x + b * c
k = (random.randint(1, 100) + z) * 5
print("k ravno " + str(k))
for m in range(1000):
    k = k + m
k = k / 12
print("k ravno " + str(k))
