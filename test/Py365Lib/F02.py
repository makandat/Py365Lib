#!/usr/bin/env python3
from Py365Lib import Common, FileSystem

# コマンドライン引数のチェック
if Common.count_args() == 0 :
  Common.stop(9, "ディレクトリを指定してください。")

# エラーコード (0 はエラーなし)
err = 0

#  パラメータ取得例
dirName = Common.args()[0]
Common.esc_print(Common.ESC_FG_CYAN, dirName)

# ファイルが存在するか確認
if not FileSystem.exists(dirName) :
  Common.stop(8, "ディレクトリが存在しません。")
    
# ディレクトリ内のファイル一覧を取得する。
Common.esc_print(Common.ESC_FG_GREEN, "ファイル一覧")
files = FileSystem.listFiles(dirName)
for fn in files :
    print(fn)

# ディレクトリ内のサブディレクトリ一覧を取得する。
Common.esc_print(Common.ESC_FG_YELLOW, "ディレクトリ一覧")
dirs = FileSystem.listDirectories(dirName)
for d in dirs :
    print(d)
    
# 終了コードを設定
exit(err)
