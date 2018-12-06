#!/usr/bin/python3
from Py365Lib import Common, FileSystem as fs
from pprint import pprint

FILE = "/home/user/temp/test.json"

# JSON ファイルを書く。
data = [
 {"type":"label", "name":"label1", "text":"LABEL", "left":15, "top":4},
 {"type":"button", "name":"ok_button", "text":" OK ", "click":100 }
]

fs.writeJson(FILE, data)
print("Wrote " + FILE)

# JSON ファイルを読む。
if fs.exists(FILE) :
  data = fs.readJson(FILE)
  pprint(data)
else :
  print(FILE + " not found.")

