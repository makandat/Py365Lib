#!/usr/bin/env python3
from Py365Lib import Common

# コマンドライン引数のチェック
if Common.count_args() == 0 :
  Common.stop(9, "パラメータを指定してください。")

# エラーコード (0 はエラーなし)
err = 0

#  パラメータ取得例
fileName = Common.args(0)
print(fileName)

try :
  # ファイルの内容を表示する。
  Common.printFile(fileName) 
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


