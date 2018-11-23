#!/usr/bin/python3
# -*- code=utf-8 -*-
#  テストプログラム DateTime
import sys
from Py365Lib import Common, DateTime as dt
import time

# テスト番号取得
if Common.count_args() == 0 :
    Common.stop(9, "テスト番号を指定してください。")
else :
    testNo = int(Common.args()[0])
    Common.esc_print(Common.ESC_FG_GREEN, testNo)

if testNo == 1 :
    ti = dt.DateTime("2018-09-15 12:00:00")
    print(ti.toString())
    now = dt.now()
    print(now)
    utc = dt.utc()
    print(utc)
elif testNo == 2 :
    ti = dt.DateTime("2018-09-15 12:00:00")
    assert ti.year == 2018, "testNo2 year"
    assert ti.month == 9, "testNo2 month"
    assert ti.day == 15, "testNo2 day"
    assert ti.hour == 12, "testNo2 hour"
    assert ti.minute == 0, "testNo2 minute"
    assert ti.second == 0, "testNo2 second"
    assert ti.dayOfweek == 5, "testNo2 dayOfweek"
    print("Test #2 OK")
elif testNo == 3 :
    ti = dt.DateTime("2018-09-15 12:00:00")
    ti.addDays(2)
    print(ti.toString())
    ti.addWeeks(1)
    print(ti.toString())
    ti.addHours(3)
    print(ti.toString())
    ti.addMinutes(30)
    print(ti.toString())
    ti.addSeconds(30)
    print(ti.toString())
elif testNo == 4 :
    t1 = dt.DateTime("2018-09-15 12:00:00")
    print(t1.timestamp)
else :
    print("不正なテスト番号です。")
