#!/usr/bin/env python3
import sys
from Py365Lib import *

key = Common.readline("環境変数の名前を入力してください。>")
try :
  value = Common.get_env(key)
  print("{0} : {1}".format(key, value))
except :
  Common.esc_print("red", "例外を検出。")
