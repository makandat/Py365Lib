#!/usr/bin/env python3
from Py365Lib import *
from pprint import pprint

# v1.10 で追加した部分文字列関数

str1 = "0123456789ABCDEF"
assert Text.substring(str1, 0, 4) == "0123"
assert Text.substring(str1, 10, 2) == "AB"
assert Text.substring(str1, 14, 4) == "EF"

assert Text.substr(str1, 0, 3) == "0123"
assert Text.substr(str1, 10, 13) == "ABCD"
assert Text.substr(str1, 14, 20) == "EF"
assert Text.substr(str1, 20, 10) == ""

assert Text.left(str1, 10) == "0123456789"
assert Text.right(str1, 10) == "6789ABCDEF"

assert Text.str_count("2018/01/12", "/") == 2
assert Text.str_count("2018//01//12", "//") == 2

print("Test OK")
