#!/usr/bin/env python3
from Py365Lib import Text
from pprint import pprint

str1 = "-rw-r--r-- 1 user user  406 11月 22 11:02 A02.log"

# 第一引数が含まれるか
b = Text.re_contain(r"^.*\.log$", str1)
print(b)
b = Text.re_contain(r"^.*\.py$", str1)
print(b)
# 最初の一致オブジェクトを取得
m = Text.re_search(r"^.*user.*", str1)
pprint(m)
m = Text.re_search(r"^.*USER.*", str1)
pprint(m)
# 文字列を分割
a1 = Text.re_split(r"\s+", str1)
pprint(a1)
# 文字列を置換
str2 = Text.re_replace(r"\s+", "~", str1)
print(str2)
