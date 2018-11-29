#!/usr/bin/env python3
#  HTApp のテスト (1)
import os
import urllib
import http.server
import HTApp
from pprint import pprint
from syslog import syslog

# / のハンドラ
def root(path) :
  html = """<html>
<head>
 <meta charset="utf-8" />
 <title>HTApp1</title>
 <style>
  body {
    margin-left: 5%;
    margin-right: 5%;
  }
  h1 {
    padding: 8px;
    color: crimson;
  }
 </style>
</head>
<body>
 <h1>HTApp1 (test_HTApp1.py)</h1>
 <p>root (/) の応答</p>
 <ul>
   <li><a href="/about">/about</a></li>
 </ul>
</body>
</html>
  """
  return ('text/html', html)

# /about のハンドラ
def about(path) :
  with open(HTApp.TEMPLATES + "/about.html") as f :
    html = f.read()
  # AppConf の内容を表示する。
  itemlist = ""
  for k, v in conf.items() :
    itemlist += HTApp.tag("li", f"{k}: {v}")
  html = html.replace("(*appconf*)", itemlist)
  return ('text/html', html)


# 開始
try :
  #  設定ファイルを読む。
  conf = HTApp.readConf()
  #  ハンドラを登録する。
  HTApp.routes['/'] = root
  HTApp.routes['/about'] = about
  #  サーバを作成
  server_name = conf['server_name']
  port = int(conf['port'])
  server = http.server.HTTPServer((server_name, port), HTApp.HTApp)
  print("START Server. Port=%d" % port)
  #  リクエスト待ち
  server.serve_forever()
except KeyboardInterrupt :
  print()
