from functools import reduce

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def mapFn(x):
    return x*x
print(list(map(mapFn, num)))

def testMap(x):
    return x+1
print(list(map(testMap, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

num2 = [1, 2, 3]
def reduceFn(x, y):
    return x+y
print(reduce(reduceFn, num2))
print(sum(num))

def char2num(s):
    dict