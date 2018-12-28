#!/usr/bin/env python3
#  Ajax
import http.server
#import http.cookies
from Py365Lib import HTApp
import json
import urllib.parse

MAXBYTES = 1024 * 16

# / のハンドラ
def root(path) :
  HTApp.vars['result'] = ""
  html = HTApp.set_template('ajax_fahren.html')
  return ('text/html', html)

# フォームのハンドラ
def convert(path) :
  html = HTApp.set_template('ajax_fahren.html')
  data = ""
  try :
    n = path.index('?')
    data = path[n+1:len(path)]
  except :
    pass
  param = urllib.parse.parse_qs(data)
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
