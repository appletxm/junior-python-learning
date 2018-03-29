#!/usr/bin/env python3
#- * -coding: utf - 8 - * -

def trim(str):
    if str[:1] != ' ' and str[-1:] != ' ':
        return str
    elif str[:1] == ' ':
        return trim(str[1:])
    elif str[-1:] == ' ':
        return trim(str[:-1])
    else:
        pass

afterTrim = trim('  ab c  ')

print(afterTrim)
print(len(afterTrim))


myList = {
    'a': '1111',
    'b': '22222'
}

for key, val in myList.items():
    print(key, val)

print([x * x
    for x in range(1, 11) if x % 2 == 0
])
print([m + n
    for m in 'ABC'
    for n in 'XYZ'
])


d = {
    'x': 'A',
    'y': 'B',
    'z': 'C'
}
for k, v in d.items():
    print(k, '=', v)

L1 = ['Hello', 'World', 18, 'Apple', None]
print(L1[2::2])
print('====', list(L1))
# newL1 = [subL for subl in L1]

strNew = ' ooo pp 09  '
print(strNew.strip(), '==', strNew.lstrip(), '==', strNew.rstrip())


myNumbers = [9, 3, 1, 2, 6, 7]
def iteration(iterater):
    obj = {'max':0, 'min':0}
    for num in myNumbers:
        if num > obj['max']:
            obj['max'] = num
        elif num < obj['min']:
            obj['min'] = num
        else:
            pass
        return obj

print('****', iteration(myNumbers))

genNumbers = [1, 2, 3, 4, 5]
g = (x * x for x in genNumbers)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

oddGen = odd()
for myGen in oddGen:
    print(myGen)
