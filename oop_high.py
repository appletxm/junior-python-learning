#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

  def __init__(self):
    self._birth = 0

  def get_score(self):
    return self._score

  def set_score(self, value):
    if not isinstance(value, int):
        raise ValueError('score must be an integer!')
    if value < 0 or value > 100:
        raise ValueError('score must between 0 ~ 100!')
    self._score = value

  @property
  def birth(self):
    return self._birth

  @birth.setter
  def birth(self, value):
    self._birth = value

  @property
  def age(self):
    return 2015 - self._birth

txm = Student()
txm.set_score(80)
print('----score is',(txm.get_score()))
print('@@@@', txm.birth)
# txm.age = 99

class Screen(object):
  def __init__(self):
    self._width = 0
    self._height = 0

  @property
  def width(self):
    return self._width

  @width.setter
  def width(self, value):
    self._width = value

  @property
  def height(self):
    return self._height

  @height.setter
  def height(self, value):
    self._height = value
  
  @property
  def resolution(self):
    return self._width * self._height

myScreen = Screen()
myScreen.width = 10
myScreen.height = 20
print(myScreen._width, myScreen._height)
print(myScreen.resolution)

