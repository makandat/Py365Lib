#!/usr/bin/env python3
import sys
from Py365Lib import Common, FileSystem 

# ログファイルの名前を決める。
logFile = FileSystem.changeExt(sys.argv[0], ".log")
print("ログファイル名：" + logFile)

# ロガーを初期化する。
Common.init_logger(logFile)

# ログにメッセージを出力する。
Common.log("テスト用")
Common.log("テスト テスト テスト")
Common.log("test Test TEST")

# ログにエラーメッセージを出力する。
Common.error("テスト：エラーメッセージ")

print("ログ出力終わり。内容は下記の通り。")

# ログファイルの内容を表示する。
log_content = FileSystem.readAllText(logFile)
print(log_content)
