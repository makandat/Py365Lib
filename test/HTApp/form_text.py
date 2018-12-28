#!/usr/bin/env python3
#  テキストボックスとボタンを持つフォーム
import urllib
import http.server
from Py365Lib import HTApp

#  "/" ハンドラ
def root(path) :
  HTApp.vars['path'] = path
  HTApp.vars['result'] = ''
  html = HTApp.set_template('form_text.html')
  return ('text/html', html)

# "/form_text_action" ハンドラ
def form_text_action(path) :
  HTApp.vars['result'] = ''
  if 'text1' in HTApp.params.keys() :
    HTApp.vars['result'] = HTApp.params['text1'].title()
  HTApp.vars['path'] = path
  html = HTApp.set_template('form_text.html')
  return ('text/html', html)

# 開始
try :
  #  設定ファイルを読む。
  conf = HTApp.readConf()
  #  ハンドラを登録する。
  HTApp.routes['/'] = root
  HTApp.routes['/form_text_action'] = form_text_action
  #  サーバを作成
  server_name = conf['server_name']
  port = int(conf['port'])
  server = http.server.HTTPServer((server_name, port), HTApp.HTApp)
  print("START Server. Port=%d" % port)
  #  リクエスト待ち
  server.serve_forever()
except KeyboardInterrupt :
  print()
