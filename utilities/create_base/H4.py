#!/usr/bin/env python3
#  HTApp のテスト (4)
import os
import http.server
import http.cookies
import HTApp
import urllib.parse as urlparse
from pprint import pprint
from syslog import syslog

# / のハンドラ
def root(path) :
  with open(HTApp.TEMPLATES + "/H4.html") as f :
    html = f.read()
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
