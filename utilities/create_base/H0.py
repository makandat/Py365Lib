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
 <title>H0</title>
 <style>
  body {
    margin-left: 5%;
    margin-right: 5%;
  }
  h1 {
    padding: 8px;
    color: coral;
    text-align: center;
  }
  .message {
    font-size: 5em;
    color: orchid;
    text-align: center;
  }
 </style>
</head>
<body>
 <h1>(H0.py)</h1>
 <br />
 <p class="message">Hello, world!</p>
</body>
</html>
  """
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
