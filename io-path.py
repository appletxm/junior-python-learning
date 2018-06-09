#!/usr/bin/env python3
#- * -coding: utf - 8 - * -

import os
import json

print(os.path.abspath('.'))

d = dict(name='Bob', age=20, score=88)
jsonStr = json.dumps(d)
print(jsonStr)
print(json.loads(jsonStr))
