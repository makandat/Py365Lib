#!/usr/bin/env python3
# -*- code=utf-8 -*-
# WebPage クラスのテスト (1)
#   MySQL を利用
import WebPage as page
import FileSystem as fsys
import MySQL

class TestPage(page.WebPage) :
  # コンストラクタ
  def __init__(self, template) :
    super().__init__(template)
    try :
      self.__mysql = MySQL.MySQL()
      rows = self.__mysql.query("SELECT `date`, FORMAT(payment, 0) AS payment, info FROM smbcvisa")
      self.vars['result'] = ""
      # クエリー
      self.getResult(rows)
      self.vars['message'] = "クエリー OK"
    except :
      self.vars['message'] = "致命的エラーを検出。詳しくは Apache2 ログを参照。"

  # クエリー結果を表にする。
  def getResult(self, rows) :
    result = ""
    for row in rows :
      result += page.WebPage.table_row(row)
    self.vars['result'] = result
    return

# メイン開始位置
wp = TestPage('templates/template1.html')
wp.echo()
