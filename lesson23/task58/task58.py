import random
import numpy as np
import pandas
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

def f1():
    df = pandas.read_csv('iq.csv')
    years_of_education = df['years_of_education'][:, np.newaxis]
    years_train, years_test, iq_train, iq_test = train_test_split(years_of_education, df['iq'], test_size=0.2)

    model = linear_model.LinearRegression()
    model.fit(years_train, iq_train)

    print('y(iq) = k * x(years_of_education) + b')
    k = model.coef_[0]
    b = model.intercept_
    print('k = ' + str(k) + '\nb = ' + str(b))

    print('iq = ' + str(k) + ' * years_education + ' + str(b))

    iq_predicted = model.predict(years_test)
    score = r2_score(iq_test, iq_predicted)
    print('Точность: %s' % score)

    print('\n\n')
    input_years = input('Введите количество лет обучения: ')
    print_iq = float(input_years) * k + b
    print('Ваш приблизительный iq: ' + str(int(print_iq)))

f1()