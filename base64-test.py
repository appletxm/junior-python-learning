#!/usr/bin/env python3
#- * -coding: utf - 8 - * -

from base64 import b64encode, b64decode, urlsafe_b64encode, urlsafe_b64decode
str64 = b64encode(b'binary\x00string')
print(str64)

strD64 = b64decode(str64)
print(strD64)


safe64 = urlsafe_b64decode(b'i\xb7\x1d\xfb\xef\xff')