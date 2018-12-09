#!/usr/bin/python3
# -*- coding=utf-8 -*-
#  MySQL クラスのテスト
from Py365Lib import MySQL as mysql
import sys

# テスト番号取得
if len(sys.argv) == 1 :
    print("テスト番号を指定してください。")
    exit(9)
else :
    testNo = int(sys.argv[1])

client = mysql.MySQL()

if testNo == 1 :
    print(client.connectInfo)
elif testNo == 2 :
    rows = client.query("SELECT * FROM m_tables")
    if client.rows > 0 :
        for row in rows :
            print(row)
elif testNo == 3:
    n = client.execute("INSERT INTO YJFX_Asset(`date`,`asset`,`profit_loss`) VALUES('2011-09-16',4574314,-874320)")
    print(n)
elif testNo == 4:
    n = client.getValue("SELECT count(*) FROM YJFX_Asset")
    print(n)
elif testNo == 5 :
    cur = client.cursor("SELECT `database`, name FROM m_tables")
    row = cur.fetchone()
    print(row[0] + "." + row[1])
    rows = cur.fetchmany(3)
    for i in range(3) :
      print(rows[i][0] + "." + rows[i][1])
else :
    print("不正なテスト番号です。")
