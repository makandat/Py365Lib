#!/usr/bin/env python3
#  HTApp のテスト (5)
#    Ajax
import os, io
import http.server
import http.cookies
import HTApp
import json
import urllib.parse as urlparse
from pprint import pprint
from syslog import syslog

MAXBYTES = 1024 * 16

# / のハンドラ
def root(path) :
  with open(HTApp.TEMPLATES + "/H5.html") as f :
    html = f.read()
  HTApp.vars['result'] = ""
  html = HTApp.embed(html)
  return ('text/html', html)

# フォームのハンドラ
def convert(path) :
  with open(HTApp.TEMPLATES + "/H5.html") as f :
    html = f.read()
  data = ""
  try :
    n = path.index('?')
    data = path[n+1:len(path)]
  except :
    pass
  param = urlparse.parse_qs(data)
  f = float(param['fahren'][0])
  c = 5.0 / 9.0 * (f - 32.0)
  result = '{"result":' + str(c) + "}"
  return ('application/json', result)

# 開始
try :
  #  設定ファイルを読む。
  conf = HTApp.readConf()
  #  ハンドラを登録する。
  HTApp.routes['/'] = root
  HTApp.routes['/Fahren'] = convert
  #  サーバを作成
  server_name = conf['server_name']
  port = int(conf['port'])
  server = http.server.HTTPServer((server_name, port), HTApp.HTApp)
  print("START Server. Port=%d" % port)
  #  リクエスト待ち
  server.serve_forever()
except KeyboardInterrupt :
  print()
