#!/usr/bin/env python3
from Py365Lib import DateTime as dt, Common, Text
from pprint import pprint

# 現在の日時を得る。DateTime クラスをインスタンス化するとその中身が現在の日時に設定される。
dt1 = dt.DateTime()
print(dt1.toString())

# 現在の日時を得る。
print("今の日時：{0:%x %X}".format(dt.now()))

# 日付の要素
print("{0}/{1}/{2}".format(dt1.year, dt1.month, dt1.day))
print("{0}:{1}:{2}".format(dt1.hour, dt1.minute, dt1.second))
