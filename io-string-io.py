#!/usr/bin/env python3
#- * -coding: utf - 8 - * -

from io import StringIO
f = StringIO()

f.write('hello')
f.write(' mmtxm')
f.write(' mmtxm !')

print(f.getvalue())

fline = StringIO('Hello!\nHi!\nGoodbye!')
while True:
  s = fline.readline()
  if s == '':
    break
  print(s)