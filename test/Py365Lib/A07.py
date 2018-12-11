#!/usr/bin/env python3
from Py365Lib import *
from pprint import pprint

# JSON 文字列をオブジェクトにする。
data = '''[
 {"type":"label", "name":"Label1", "text":"Label1", "left":20, "top":3},
 {"type":"button", "name":"btnOK", "text":" OK ", "left":20, "top":4}
]'''
obj = Common.from_json(data)
pprint(obj)

# オブジェクトを JSON 文字列にする。
json = Common.to_json(obj)
print(json)
