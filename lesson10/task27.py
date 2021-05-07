import re
print(1)
if re.match('^ $', 'a'):
    print('является')
else:
    print('не является')

print(2)
if re.match('^\d$', '10'):
    print('является')
else:
    print('не является')

print(3)
if re.match('^\d\d$', '10'):
    print('является')
else:
    print('не является')

print(4)
if re.match('^   $', '   '):
    print('является')
else:
    print('не является')

print(5)
if re.match('^a\dv$', 'a4v'):
    print('является')
else:
    print('не является')
