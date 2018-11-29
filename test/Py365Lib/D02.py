#!/usr/bin/env python3
from Py365Lib import DateTime as dt, Common, Text
from pprint import pprint

# 現在の日時を得る。DateTime クラスをインスタンス化するとその中身が現在の日時に設定される。
dt1 = dt.DateTime()
print(dt1.toString())

# 明日
dt1 = dt.DateTime("2018-01-01 00:00:00")
dt1.addDays(1)
print(dt1.toDateString())

# 昨日
dt1 = dt.DateTime("2018-01-01 00:00:00")
dt1.addDays(-1)
print(dt1.toDateString())

# １時間後
dt1 = dt.DateTime("2018-01-01 00:00:00")
dt1.addSeconds(3600)
print(dt1.toTimeString())

# １時間前
dt1 = dt.DateTime("2018-01-01 00:00:00")
dt1.addSeconds(-3600)
print(dt1.toTimeString())
