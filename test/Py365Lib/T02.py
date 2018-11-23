#!/usr/bin/env python3
from Py365Lib import *
from pprint import pprint

str1 = """-rw-r--r-- 1 user user  406 11月 22 11:02 A02.log
-rwxr-xr-x 1 user user  691 11月 22 11:02 A02.py
-rwxr-xr-x 1 user user  611 11月 22 11:23 A03.py
-rwxr-xr-x 1 user user  505 11月 22 11:42 A04.py
-rwxr-xr-x 1 user user 1062 11月 22 14:17 F01.py
-rwxr-xr-x 1 user user  940 11月 22 15:27 F02.py
-rwxrwxr-x 1 user user  552 11月 22 17:12 F03.py
-rwxr-xr-x 1 user user  824 11月 22 17:41 F04.py
-rwxr-xr-x 1 user user  512 11月 23 17:14 T01.py
-rwxr-xr-x 1 user user  135 11月 23 20:03 T02.py
"""

b = Text.re_contain("\\d\\d:\\d\\d", str1)
print(b)
m = Text.re_search("rwxrwxr", str1)
pprint(m)
