import re
print('\n1')
if re.match('^[HMBP][HMBP]\d\d\d\d\d\d\d$', 'HP3832199'):
    print('является')
else:
    print('не является')

print('\n2')
if re.match('^(Привет|Добрый день|Салют) дорогой юзер$', 'Привет дорогой юзер'):
    print('является')
else:
    print('не является')

print('\n3')
if re.match('^(\-\d*.\d*|\d*.\d*|\d|\-\d)(\+|\-|\/|\*)(\-\d*.\d*|\d*.\d*|\d|\-\d)$', '1.2+2.22'):
    print('является')
else:
    print('не является')
