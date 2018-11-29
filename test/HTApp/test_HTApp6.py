#!/usr/bin/env python3
#  HTApp のテスト (6)
#    POST のテスト
import os, io
import http.server
import http.cookies
import HTApp
import urllib.parse as urlparse
from pprint import pprint
from syslog import syslog

MAXBYTES = 1024 * 16

# / のハンドラ
def root(path) :
  with open(HTApp.TEMPLATES + "/index6.html") as f :
    html = f.read()
  HTApp.vars['message'] = ""
  html = HTApp.embed(html)
  return ('text/html', html)

# フォームのハンドラ
def PostHandler(path) :
  with open(HTApp.TEMPLATES + "/index6.html") as f :
    html = f.read()
  # param = io.BufferedIOBase(HTApp.posted_file).read(MAXBYTES)
  HTApp.vars['message'] = "POST のパラメータはサポートされません。"
  html = HTApp.embed(html)
  return ('text/html', html)

# 開始
try :
  #  設定ファイルを読む。
  conf = HTApp.readConf()
  #  ハンドラを登録する。
  HTApp.routes['/'] = root
  HTApp.routes['/Post'] = PostHandler
  #  サーバを作成
  server_name = conf['server_name']
  port = int(conf['port'])
  server = http.server.HTTPServer((server_name, port), HTApp.HTApp)
  print("START Server. Port=%d" % port)
  #  リクエスト待ち
  server.serve_forever()
except KeyboardInterrupt :
  print()
