#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('haha')
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

# birth = int(input('birth: '))
# if birth < 2000:
#     print('00前')
# elif birth > 1000:
#     print('10000')
# else:
#     print('00后')

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

myNames = [1, 4, 2, 3]
print(myNames)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print('total is %s' % sum)

myList = range(4)
myTotal = 0
for y in myList:
    myTotal += y
print(myTotal)

print('===========')
for cellName in names:
    print(cellName)
print('============')

print('==========dictionary====')
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print('%s' % (d['Michael']))
if 'Bob' in d:
    print('find Bob\'s score is %.2f %s' % (d['Michael'], d.get('Tracy')))
    # print('find Bob\'s score is {0:.2f}'.format(d['Michael']))
else:
    print('can\'t find Bob\'s score')
