# -*- code=utf-8 -*-
# Version 0.50  2018-09-12
# Version 1.00  2018-10-03
# Version 1.10  2018-12-01
# Version 1.20  2019-04-09
# version 2.0.0 2023-03-21
#    To install mysqlclient
#  sudo pip3 install mysqlclient
import MySQLdb
import json

class MySQL :
  CONF = "mysqlclient.json"

  # コンストラクタ
  def __init__(self, user="", password="", database="", host="localhost") :
    # パラメータが無効の場合は、CONF から取得する。
    if user == "" :
      with open(MySQL.CONF, "r") as f:
        conf = json.load(f)
        self._client = MySQLdb.connect(user=conf["user"], password=conf["password"], host=conf["host"], database=conf["user"])
    else :
      # 接続する。
      self._client = MySQLdb.connect(host, user, password, database)
    # カーソルを取得する。
    self._cursor = self._client.cursor()
    return

  # クエリーを行う。
  def query(self, sql) :
    self._cursor.execute(sql)
    rows = self._cursor.fetchall()
    return rows

  # コマンドを実行する。
  def execute(self, sql) :
    n = 0
    try :
      n = self._cursor.execute(sql)
      self._client.commit()
    except :
      self._client.rollback()
      raise
    return n

  # 値を1つだけ返すクエリーを実行し、その値を得る。
  def getValue(self, sql) :
    result = None
    self._cursor.execute(sql)
    row = self._cursor.fetchone()
    return row[0]

  # 行を1つだけ返すクエリーを実行し、その値を得る。
  def getRow(self, sql) :
    result = None
    self._cursor.execute(sql)
    rows = self._cursor.fetchone()
    return rows

  # カーソルを閉じる。
  def cursorClose(self) :
    self._cursor.close()
