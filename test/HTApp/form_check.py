#!/usr/bin/env python3
#  チェックボックスとボタンを持つフォーム
import urllib
import http.server
from Py365Lib import HTApp

#  "/" ハンドラ
def root(path) :
  HTApp.vars['path'] = path
  HTApp.vars['result'] = ''
  # チェックボックスをすべてクリア
  HTApp.params = {}
  for i in range(1, 5) :
    HTApp.vars["check" + str(i)] = ""
  html = HTApp.set_template('form_check.html')
  return ('text/html', html)

# "/form_check_action" ハンドラ
def form_check_action(path) :
  # チェックされている項目を表示
  result = ""
  for v in HTApp.params.values() :
    result += (v + ";")
  HTApp.vars['result'] = result
  # チェックボックスの状態を復元
  for i in range(1, 5) :
    HTApp.vars["check" + str(i)] = ""
  for k in HTApp.params.keys() :
    HTApp.vars[k] = "checked"
  # path を表示
  HTApp.vars['path'] = path
  html = HTApp.set_template('form_check.html')
  return ('text/html', html)

# 開始
try :
  #  設定ファイルを読む。
  conf = HTApp.readConf()
  #  ハンドラを登録する。
  HTApp.routes['/'] = root
  HTApp.routes['/form_check_action'] = form_check_action
  #  サーバを作成
  server_name = conf['server_name']
  port = int(conf['port'])
  server = http.server.HTTPServer((server_name, port), HTApp.HTApp)
  print("START Server. Port=%d" % port)
  #  リクエスト待ち
  server.serve_forever()
except KeyboardInterrupt :
  print()
