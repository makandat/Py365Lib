#!/usr/bin/env python3
# cookie 
import os
import http.server
import http.cookies
from Py365Lib import HTApp
import urllib.parse as urlparse

# / のハンドラ
def root(path) :
  html = HTApp.set_template('cookie.html', False)
  if 'count' in HTApp.cookies :
    count = int(HTApp.cookies['count']) + 1
  else :
    count = 0
  HTApp.cookies['count'] = str(count)
  HTApp.vars['count'] = str(count)
  html = HTApp.embed(html)
  return ('text/html', html)


# 開始
try :
  #  設定ファイルを読む。
  conf = HTApp.readConf()
  #  ハンドラを登録する。
  HTApp.routes['/'] = root
  HTApp.routes['/AppCreator'] = root
  #  サーバを作成
  server_name = conf['server_name']
  port = int(conf['port'])
  server = http.server.HTTPServer((server_name, port), HTApp.HTApp)
  print("START Server. Port=%d" % port)
  #  リクエスト待ち
  server.serve_forever()
except KeyboardInterrupt :
  print()
