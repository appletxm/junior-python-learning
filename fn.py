#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

print(math.cos(45))


def myFn(x):
    if x > 0:
        return x
    else:
        return -x


print(myFn(-3))


def voidFn():
    pass


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


voidFn()


def multipleRturn(x=1, y=2):
    return x * 2, y * 2


x, y = multipleRturn()
print(x, y)


def pow(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print('pow(5, 2)', pow(5, 2))
print('pow(5, 3)', pow(5, 3))
print('pow(6)', pow(6))


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print('add_end', add_end())


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum


calcNumbers = [1, 2, 3, 4, 5]
print('=====calc', calc(*calcNumbers))


def person(name, age, *kw):
    print('---name:', name, 'age:', age, 'other:', kw)


person('txm', 30, 4, 5)


def personNew(name, age, **kw):
    print('---name:', name, 'age:', age, 'other:', kw)


personNew('txm', 30, worker='IT', gender='fmale')


def personMy(name, age, *, city, job):
    print(name, age, city, job)


personMy('txm', 30, city='guangzhou', job='programmer')
