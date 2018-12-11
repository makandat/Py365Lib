#!/usr/bin/env python3
from Py365Lib import *

# バイト列を文字列にする。
data = b'ABCDEF'
str = Common.from_bytes(data)
print(str)
print(Common.is_str(str))

# 文字列をバイト列にする。
str = "01234"
data = Common.to_bytes(str)
print(data)
