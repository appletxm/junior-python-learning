#!/usr/bin/env python3
#- * -coding: utf - 8 - * -

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
q.pop()
print(q)
q.popleft()
print(q)

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'txm'
dd['key2'] = 'abc'
print(dd['key1'], dd['key3'])

d = dict([('a', 1), ('c', 3), ('b', 2)])
od = OrderedDict([('a', 1), ('c', 3), ('b', 2)])

print(d, od)

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()))


class LastUpdatedOrderedDict(OrderedDict):

  def __init__(self, capacity):
    super(LastUpdatedOrderedDict, self).__init__()
    self._capacity = capacity

  def __setitem__(self, key, value):
    containsKey = 1 if key in self else 0
    if len(self) - containsKey >= self._capacity:
        last = self.popitem(last=False)
        print('remove:', last)
    if containsKey:
        del self[key]
        print('set:', (key, value))
    else:
        print('add:', (key, value))
    OrderedDict.__setitem__(self, key, value)

c = Counter()
for ch in 'programming':
  c[ch] = c[ch] + 1
print(c)