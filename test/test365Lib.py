#!/usr/bin/env python3
from Py365Lib import *

def callback() :
  print("callback")

# args() 関数、stop() 関数のテスト
if Common.count_args() == 0 :
  Common.stop(9, "コマンド引数がありません。")
else :
  for s in Common.args() :
    Common.esc_print(Common.ESC_FG_GREEN, s)

testNo = int(Common.args()[0])

if testNo == 1 :
  # ログのテスト
  Common.init_logger()
  print(Common.LOGFILE)
  Common.log("ログのテスト")
  Common.error("ログのエラー")

  # exec(cmd), shell(cmd)
  rc = Common.exec(['tail', '-n', '4', Common.LOGFILE])
  print(rc)
  print(Common.shell(['ls', '/']))

  # isset(v)
  ooo = None
  print(Common.isset(ooo))
  print(Common.isset(rc))
elif testNo == 2 :
  # is_str(x) etc.
  print(Common.is_str(0))
  print(Common.is_str('0'))
  print(Common.is_int('0'))
  print(Common.is_int(0))
  print(Common.is_float('1.5'))
  print(Common.is_float(1.5))
  print(Common.is_bool(0))
  print(Common.is_bool(False))
elif testNo == 3 :
  # syslog, setTimeout, get_env
  Common.syslog_out("setTimeout test")
  Common.set_timeout(0.5, callback)
  Common.syslog_out("OK")
  lang = Common.get_env("LANG")
  Common.syslog_out(lang)
  print("LANG=" + lang)
  Common.sleep(2)
  print("sudo cat /var/log/syslog")
else :
  print("不正な番号です。")

print('Done.')

