#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
  def parentFn(self):
    print('parentFn...')

# 大类:
class Mammal(Animal):
  pass

class Bird(Animal):
  pass

class Runnable(object):
  def run(self):
    print('Running...')

class Flyable(object):
  def fly(self):
    print('Flying...')

class Dog(Mammal, Runnable):
  pass

class Bat(Mammal, Flyable):
  pass

dog = Dog()
dog.run()
dog.parentFn()