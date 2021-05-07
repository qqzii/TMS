import pandas

info = pandas.read_csv("D:/TMS/lesson13/info.csv")
marks = pandas.read_csv("D:/TMS/lesson13/marks.csv")

def f1():
    know_marks = info.merge(marks, left_on='id', right_on='id2').shape[0]
    all = info.shape[0]
    print(all-know_marks)

f1()

def f2():
    q = info[(info['race'] == 'group A')]
    quantity = q.merge(marks, left_on='id', right_on='id2').shape[0]
    w = info[(info['race'] == 'group A')]
    e = w.merge(marks, left_on='id', right_on='id2')
    sum = e['math'].sum()
    print(sum/quantity)

f2()

def f3():
    new = info.merge(marks, left_on='id', right_on='id2', how='outer')
    print(new.shape[0])

f3()

def f4():
    new = info.merge(marks, left_on='id', right_on='id2', how='left')
    print(new.shape[0])

f4()

def f5():
    new = info.merge(marks, left_on='id', right_on='id2', how='right')
    print(new.shape[0])

f5()
