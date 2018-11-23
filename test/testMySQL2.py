#!/usr/bin/python3
# -*- coding=utf-8 -*-
#  MySQL クラスのテスト (2)
import MySQL as mysql
import sys

# テスト番号取得
if len(sys.argv) == 1 :
    print("テスト番号を指定してください。")
    exit(9)
else :
    testNo = int(sys.argv[1])

client = mysql.MySQL("user", "ust62kjy", "user", "localhost")

if testNo == 1 :
    # 接続情報を表示
    print(client.connectInfo)
elif testNo == 2 :
    # SELECT クエリー
    rows = client.query("SELECT * FROM smbcvisa")
    if client.rows > 0 :
        for row in rows :
            print(row[0] + "," + str(row[1]))
elif testNo == 3:
    # SQL (INSERT) 実行
    n = client.execute("INSERT INTO smbcvisa VALUES('2018-09-11',4574314, 'テスト')")
    print(n)
elif testNo == 4 :
    # カーソルの使用
    cur = client.cursor("SELECT * FROM smbcvisa")
    for (dt, pay, info) in cur :
        print(dt, pay, info)
else :
    print("不正なテスト番号です。")
