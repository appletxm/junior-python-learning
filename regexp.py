#!/usr/bin/env python3
#- * -coding: utf - 8 - * -

import re
print(re.match('^\d{3,8}$', '123456'))

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m, m.group(1), m.group(2))

tr = re.compile(r'(\d{1,2})\:(\d{1,2}):(\d{1,2})$')
t = tr.match('19:05:30')