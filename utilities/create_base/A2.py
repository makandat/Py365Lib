#!/usr/bin/env python3
import sys
from Py365Lib import *


# コメントを緑色で表示する。
def display(line) :
  s = Text.trim(line)
  if len(s) >= 1 and s[0] == '#' :
    Common.esc_print("green", line)
  else :
    print(line)
  return


# ログファイルの名前を決める。
logFile = FileSystem.changeExt(sys.argv[0], ".log")
print("ログファイル名：" + logFile)

# ロガーを初期化する。
Common.init_logger(logFile)

# ログにメッセージを出力する。
Common.log("テスト用")


# コマンドライン引数のチェック
if Common.count_args() == 0 :
  Common.error("コマンドライン引数がない。")  # エラーログ
  Common.stop(9, "パラメータを指定してください。")

# エラーコード (0 はエラーなし)
err = 0

#  パラメータ取得例
fileName = Common.args()[0]
print(fileName)

try :
  # ファイルの内容を表示する。
  FileSystem.readAllLines(fileName, display)
except Exception as e :
  # 例外発生時の処理
  Common.esc_print("red", e.args)
  err = 1


if err == 0 :
  print("正常終了。")
else :
  print("エラーを検出しました。エラーコード: {0:d}".format(err))

# 終了コードを err とする。 (0 はエラーなし)
exit(err)
