#!/usr/bin/env python3
#- * -coding: utf - 8 - * -

import os

print(os.name)
# print(os.uname)
# print(os.environ)
# print(os.environ.get('PATH'))
print(os.path.abspath('.'))
path = os.path.join('./files', 'testdir')
# os.mkdir(path)
os.rmdir(path)
