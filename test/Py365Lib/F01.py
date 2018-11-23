#!/usr/bin/env python3
from Py365Lib import *

# コマンドライン引数のチェック
if Common.count_args() == 0 :
  Common.stop(9, "ファイルを指定してください。")

# エラーコード (0 はエラーなし)
err = 0

#  パラメータ取得例
fileName = Common.args()[0]
Common.esc_print(Common.ESC_FG_CYAN, fileName)

# ファイルが存在するか確認
if not FileSystem.exists(fileName) :
  Common.stop(8, "ファイルが存在しません。")
    
# ファイルの属性を得る。
b = FileSystem.isFile(fileName)
print("ファイルかどうか： {0}".format(b))
b = FileSystem.isDirectory(fileName)
print("ディレクトリかどうか： {0}".format(b))
b = FileSystem.isLink(fileName)
print("リンクかどうか： {0}".format(b))
mode = FileSystem.getAttr(fileName)
print("ファイルモード： {0:09o}".format(mode))
owner = FileSystem.getOwner(fileName)
print("所有者： {0}".format(owner))
group = FileSystem.getGroup(fileName)
print("グループ： {0}".format(group))

# 終了コードを設定
exit(err)
