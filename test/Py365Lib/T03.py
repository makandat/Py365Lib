#!/usr/bin/env python3
from Py365Lib import Text
from pprint import pprint

# 文字列から数値への変換とフォーマット化
n = Text.parseInt("1024")
f = Text.parseDouble("-3.61e+2")
s1 = Text.format("n = {0:8d}, f = {1:10.2f}", n, f)
print(s1)

# split, join
s2 = Text.join(",", ["5098", "1989", "320", "298"])
print(s2)
a2 = Text.split(",", s2)
pprint(a2)

# contain, indexOf
s3 = "ABCDEFGHIJKL"
print(Text.contain("CD", s3))
print(Text.contain("cd", s3))
print(Text.indexOf("CD", s3))
print(Text.indexOf("1", s3))

# replace
s4 = Text.replace("GHIJ", "0123", s3)
print(s4)
