answer10t1 = (4 >= 4 or 0 != 0)
answer10t2 = (6 == 1 or 2 == 2)
answer10t3 = (True or 'ww' != 'ww')

answer10f1 = ('hi' != 'hi' or 2 * 2 == 5)
answer10f2 = (0 == 1 or 2 != 2)
answer10f3 = (0 != 0 or False)

List = [answer10t1, answer10t2, answer10t3, answer10f1, answer10f2, answer10f3]

for i in range(len(List)):
    print(str(i+1) + '.  ' + str(List[i]))
