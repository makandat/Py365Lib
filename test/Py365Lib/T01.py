#!/usr/bin/env python3
from Py365Lib import Common, Text as txt

# Text オブジェクトを構築
to = txt.Text("0123456789")

# 結合
to.append("ABCDEF")
print(to.toString())

# 部分文字列
print(to.substring(1, 4))  # 位置 1 から 4 文字分
print(to.substr(1, 4))     # 位置 1 から位置 4 まで
print(to.left(4))   # 左側 4 文字分
print(to.right(4))  # 右側 4 文字分

# 同じ文字の繰り返し
to.times('*', 10)
print(to.toString())

# クリア
to.clear()
print(to.toString())
