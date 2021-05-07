import pandas

df = pandas.read_csv('D:/TMS/lesson13/titanic.csv')

def f1():
    print(df.columns)

f1()

def f2():
    print(df.shape[0])
f2()

def f3():
    print(df[(df['Sex'] == 'male')].shape[0])

f3()

def f4():
    print(str(df[(df['Survived'] == 1)].shape[0] / df.shape[0] * 100) + ' %')

f4()

def f5():
    if df[(df['Sex'] == 'male')].shape[0] > df[(df['Sex'] == 'female')].shape[0]:
        print('Мужчин было больше')
    else:
        print('Женщин было больше')

f5()

def f6():
    a = df[(df['Survived'] == 1) & (df['Sex'] == 'male')].shape[0]
    b = df[df['Survived'] == 1].shape[0]
    print(str((a / b) * 100) + ' %')

f6()

def f7():
    surv_econom = df[(df['Survived'] == 1) & (df['Pclass'] == 3)].shape[0]
    full_econom = df[df['Pclass'] == 3].shape[0]

    surv_middle = df[(df['Survived'] == 1) & (df['Pclass'] == 2)].shape[0]
    full_middle = df[df['Pclass'] == 2].shape[0]

    surv_rich = df[(df['Survived'] == 1) & (df['Pclass'] == 1)].shape[0]
    full_rich = df[df['Pclass'] == 1].shape[0]


    print(str((surv_rich / full_rich) * 100) + ' % - столько выжило богатых людей')
    print(str((surv_middle / full_middle) * 100) + ' % - столько выжило людей среднего класса')
    print(str((surv_econom / full_econom) * 100) + ' % - столько выжило бедных людей')

f7()
