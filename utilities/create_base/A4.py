#!/usr/bin/python3
# -*- coding=utf-8 -*-
#  MySQL クラスのテスト
import MySQL as mysql
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
else :
    print("不正なテスト番号です。")
