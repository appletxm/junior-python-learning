#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import  Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month)

for name, member in Month.__members__.items():
  print(name, '=>', member, ',', member.value)

@unique
class Weekday(Enum):
  Sun = 0 # Sun的value被设定为0
  Mon = 1
  Tue = 2
  Wed = 3
  Thu = 4
  Fri = 5
  Sat = 6


class Gender(Enum):
  Male = 0
  Female = 1

class Student(object):
  def __init__(self, name, gender):
    self.name = name
    self.gender = gender

lisa = Student('Lisa', Gender.Female)
mark = Student('Mark', Gender.Male)

print(lisa.gender, mark.gender)
