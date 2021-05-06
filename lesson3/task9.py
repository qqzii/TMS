answer9t1 = (4 >= 4 and True)
answer9t2 = (6 > 1 and 2 == 2)
answer9t3 = (2 > 0.1 and 'ww' != 'w1')

answer9f1 = (4 >= 4 and False)
answer9f2 = (0 > 1 and 2 == 2)
answer9f3 = ('lol' != 'lol' and False)

List = [answer9t1, answer9t2, answer9t3, answer9f1, answer9f2, answer9f3]

for i in range(len(List)):
    print(str(i+1) + '.  ' + str(List[i]))
