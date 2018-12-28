#!/usr/bin/env python3
#  テキストボックスとボタンを持つフォーム
import urllib
import http.server
from Py365Lib import HTApp

#  "/" ハンドラ
def root(path) :
  HTApp.vars['path'] = path
  HTApp.vars['result'] = ''
  # ラジオボタンをリセット
  HTApp.vars['radio1'] = "checked"
  HTApp.vars['radio2'] = ""
  HTApp.vars['radio3'] = ""
  HTApp.vars['radio4'] = ""
  HTApp.vars['radio5'] = ""
  html = HTApp.set_template('form_radio.html')
  return ('text/html', html)

# "/form_radio_action" ハンドラ
def form_radio_action(path) :
  # チェックされている項目を表示
  result = ""
  for v in HTApp.params.values() :
    result += (v + ";")
  HTApp.vars['result'] = result
  # ラジオボタンの状態を復元
  for i in range(1, 6) :
    HTApp.vars["radio" + str(i)] = ""
  k = recover_checked()
  HTApp.vars[k] = "checked"
  # path を表示
  HTApp.vars['path'] = path
  html = HTApp.set_template('form_radio.html')
  return ('text/html', html)

def recover_checked() :
  key = ""
  if HTApp.params['radio'] == '現国' :
    key = "radio1"
  elif HTApp.params['radio'] == '古文' :
    key = "radio2"
  elif HTApp.params['radio'] == '数I' :
    key = "radio3"
  elif HTApp.params['radio'] == '物理' :
    key = "radio4"
  elif HTApp.params['radio'] == '日本史' :
    key = "radio5"
  else :
    pass
  return key

# 開始
try :
  #  設定ファイルを読む。
  conf = HTApp.readConf()
  #  ハンドラを登録する。
  HTApp.routes['/'] = root
  HTApp.routes['/form_radio_action'] = form_radio_action
  #  サーバを作成
  server_name = conf['server_name']
  port = int(conf['port'])
  server = http.server.HTTPServer((server_name, port), HTApp.HTApp)
  print("START Server. Port=%d" % port)
  #  リクエスト待ち
  server.serve_forever()
except KeyboardInterrupt :
  print()
