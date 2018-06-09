#!/usr/bin/env python3
#- * -coding: utf - 8 - * -

filePath = './files/test.txt'
chFilePath = './files/zh-cn.txt'
imgFile = './files/pic.jpg'

# try:
#   f = open(filePath, 'r')
#   print(f.read())
# finally:
#   if f:
#     f.close()

# with open(filePath, 'r') as f:
#   # print(f.readlines())
#   fileLines = f.readlines()

f = open(filePath, 'r')
fileLines = f.readlines()
print(fileLines)
for line in f.readlines():
  print(line.strip()) 

chF = open(chFilePath, 'r', encoding='gbk', errors='ignore')
print(chF.read())

imgF = open(imgFile, 'rb')
print(imgF.read())

