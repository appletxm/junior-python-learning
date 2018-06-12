#!/usr/bin/env python3
#- * -coding: utf - 8 - * -

from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)

dt = datetime(2015, 4, 19, 12, 20)
print(dt, dt.timestamp(), datetime.fromtimestamp(dt.timestamp()))

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

print(now.strftime('%a, %b %d %H:%M'))

now = now + timedelta(hours=10)
print(now.strftime('%a, %b %d %H:%M'))

now = now - timedelta(days=2, hours=12)
print(now.strftime('%a, %b %d %H:%M'))

print(datetime.utcnow())