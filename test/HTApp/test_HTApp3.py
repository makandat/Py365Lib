#!/usr/bin/env python3
#  HTApp のテスト (3)
import os
import http.server
from Py365Lib import HTApp
import urllib.parse as urlparse
from pprint import pprint
from syslog import syslog

# / のハンドラ
def root(path) :
  with open(HTApp.TEMPLATES + "/index3.html") as f :
    html = f.read()
  params = {}
  try :
    n = path.index('?') + 1
    qs = path[n:len(path)]
    params = urlparse.parse_qs(qs)
    litems = ""
    for k, v in params.items() :
      vv = v[0]
      litems += HTApp.tag("li", f"{k} = {vv}")
    html = html.replace("(*params*)", litems)
  except :
    html = html.replace("(*params*)", "")
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
