#!/usr/bin/env python3
from Py365Lib import Common, Text

# txt
txt = "0123456789"

# 結合
to = Text.concat(txt, "ABCDEF")
print(to)

# 部分文字列
print(Text.substring(to, 1, 4))  # 位置 1 から 4 文字分
print(Text.substr(to, 1, 4))     # 位置 1 から位置 4 まで
print(Text.left(to, 4))   # 左側 4 文字分
print(Text.right(to, 4))  # 右側 4 文字分

# 同じ文字の繰り返し
to = Text.times('*', 10)
print(to)

