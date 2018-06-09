#!/usr/bin/env python3
#- * -coding: utf - 8 - * -

filePath = './files/test.txt'

#cover old one
# with open(filePath, 'w') as f:
#     f.write('this is append content!')

#append
with open(filePath, 'a') as f:
    f.write('this is append content!\n')