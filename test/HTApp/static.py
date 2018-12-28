#!/usr/bin/env python3
#  スタティックなコンテンツ
import urllib
import http.server
from Py365Lib import HTApp

#  "/" ハンドラ
def root(path) :
  html = HTApp.set_template('static.html')
  return ('text/html', html)


# 開始
try :
  #  設定ファイルを読む。
  conf = HTApp.readConf()
  #  ハンドラを登録する。
  HTApp.routes['/'] = root
  #  サーバを作成
  server_name = conf['server_name']
  port = int(conf['port'])
  server = http.server.HTTPServer((server_name, port), HTApp.HTApp)
  print("START Server. Port=%d" % port)
  #  リクエスト待ち
  server.serve_forever()
except KeyboardInterrupt :
  print()
