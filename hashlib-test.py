#!/usr/bin/env python3
#- * -coding: utf - 8 - * -

from hashlib import md5

md5 = md5()
md5.update('how to use md5 1 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())