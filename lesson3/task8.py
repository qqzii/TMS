x1t = (5 > 3)
x1f = (1 > 3)

x2t = (1 < 4)
x2f = (2 < 1)

x3t = ('lol' == 'lol')
x3f = ('http' == 'www')

x4t = (4 >= 4)
x4f = (4 >= 1)

x5t = (1 <= 3)
x5f = (4 <= 0)

x6t = (x3t != x3f)
x6f = (11.2 != 11.2)

List = [x1t, x1f, x2t, x2f, x3t, x3f, x4t, x4f, x5t, x5f, x6t, x6f]

for i in range(len(List)):
    print(str(i+1) + '.  ' + str(List[i]))
