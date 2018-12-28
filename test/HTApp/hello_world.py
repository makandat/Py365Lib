#!/usr/bin/env python3
#  hello_world.py
import urllib
import http.server
from Py365Lib import HTApp

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
    color: deeppink;
    text-align:center;
    margin-top:30px;
  }
 </style>
</head>
<body>
 <h1>Hello, World!</h1>
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
