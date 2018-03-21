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
