#!/usr/bin/env python3
import Common, FileSystem

# コマンドライン引数のチェック
if Common.count_args() == 0 :
  Common.stop(9, "パラメータを指定してください。")

# エラーコード (0 はエラーなし)
err = 0

#  パラメータ取得例
fileName = Common.args()[0]
Common.esc_print("yellow", fileName)

# AppConf.ini を読む。
conf = FileSystem.readIni(fileName)

try :
  # INI ファイルの内容を表示する。
  print("host={0}".format(conf['host']))
  print("uid={0}".format(conf['uid']))
  print("pwd={0}".format(conf['pwd']))
  print("db={0}".format(conf['db']))
except Exception as e :
  # 例外発生時の処理
  Common.esc_print(Common.ESC_FG_RED, e.args)
  err = 1


if err == 0 :
  print("正常終了。")
else :
  print("エラーを検出しました。エラーコード: {0:d}".format(err))

# 終了コードを err とする。 (0 はエラーなし)
exit(err)


