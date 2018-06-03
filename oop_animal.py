#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
  def run(self):
      print('Animal is running...')

class Dog(Animal):
  # pass
  def run(self):
    print('Dog is running...')

class Cat(Animal):
  # pass
  def run(self):
    print('Cat is running...')

  def eat(self):
    print('Eating meat...')

dog = Dog()
dog.run()

cat = Cat()
cat.run()

print('@@@@@', isinstance(dog, Animal))

class MyObject(object):
  def __init__(self):
    self.x = 7
    self.my= 0
  def power(self):
    return self.x * self.x

obj = MyObject()
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
print(setattr(obj, 'my', 56))
setattr(obj, 'my', 56)
print(obj.my)


class Student(object):
  count = 0
  def __init__(self, name):
    self.name = name

s = Student('Bob')
Student.count = Student.count + 1
print(Student.count)
s2 = Student('Emily')
Student.count = Student.count + 1
print(Student.count)
