import re
print('\n1')
if re.match('^a(\-\d*.\d*|\d*.\d*|\d|\-\d)c$', 'a233c'):
    print('является')
else:
    print('не является')

print('\n2')
if re.match('^a(\-\d*.\d*|\d*.\d*|\d|\-\d|)c$', 'ac'):
    print('является')
else:
    print('не является')

print('\n3')
if re.match('^.+@\w+\.\w+$', 'artemy.morozov@gmail.ru'):
    x = re.match('^(.+)(@\w+\.\w+)$', 'artemy.morozov@gmail.ru').groups()
    count = 0
    y = ''
    while count < len(x):
        y += x[count]
        count += 1
    print(y)
else:
    raise Exception('Понимаю только email')

print('\n4')
tag = re.match('^<\w+>(\w+)<\/\w+>$', '<a>nn</a>').groups()
print(tag[0])

print('\n5')
if re.match('^(\d+)\-(\d\d|\d)\-(\d\d|\d)\s(\d\d|\d):(\d\d|\d):(\d\d|\d)$', '2018-01-09 12:24:04'):
    time = re.match('^(\d+)\-(\d\d|\d)\-(\d\d|\d)\s(\d\d|\d):(\d\d|\d):(\d\d|\d)$', '2018-01-09 12:24:04').groups()
    print(time[4])
else:
    print('Не понимаю')

print('\n6')
if re.match('^(\-\d*.\d*|\d*.\d*|\d|\-\d)(\+|\-|\/|\*)(\-\d*.\d*|\d*.\d*|\d|\-\d)$', '1.2+2.22'):
    calc = re.match('^(\-\d*.\d*|\d*.\d*|\d|\-\d)(\+|\-|\/|\*)(\-\d*.\d*|\d*.\d*|\d|\-\d)$', '1.2+2.22').groups()
    if calc[1] == '+':
        print(calc[0] + ' ' + calc[1] + ' ' + calc[2] + ' = ' + str(float(calc[0]) + float(calc[2])))
    if calc[1] == '-':
        print(calc[0] + ' ' + calc[1] + ' ' + calc[2] + ' = ' + str(float(calc[0]) - float(calc[2])))
    if calc[1] == '*':
        print(calc[0] + ' ' + calc[1] + ' ' + calc[2] + ' = ' + str(float(calc[0]) * float(calc[2])))
    if calc[1] == '/':
        print(calc[0] + ' ' + calc[1] + ' ' + calc[2] + ' = ' + str(float(calc[0]) / float(calc[2])))
else:
    print('не является арефметическим выражением...')
