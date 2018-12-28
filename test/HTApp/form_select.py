#!/usr/bin/env python3
#  リストボックスとボタンを持つフォーム
import urllib
import http.server
from Py365Lib import HTApp

#  "/" ハンドラ
def root(path) :
  HTApp.vars['path'] = path
  HTApp.vars['result'] = ''
  html = HTApp.set_template('form_select.html')
  return ('text/html', html)

# "/form_select_action" ハンドラ
def form_select_action(path) :
  # 選択されている項目を表示
  result = ""
  for v in HTApp.params.values() :
    result += (v + ";")
  HTApp.vars['result'] = result
  # path を表示
  HTApp.vars['path'] = path
  html = HTApp.set_template('form_select.html')
  return ('text/html', html)

# 開始
try :
  #  設定ファイルを読む。
  conf = HTApp.readConf()
  #  ハンドラを登録する。
  HTApp.routes['/'] = root
  HTApp.routes['/form_select_action'] = form_select_action
  #  サーバを作成
  server_name = conf['server_name']
  port = int(conf['port'])
  server = http.server.HTTPServer((server_name, port), HTApp.HTApp)
  print("START Server. Port=%d" % port)
  #  リクエスト待ち
  server.serve_forever()
except KeyboardInterrupt :
  print()
