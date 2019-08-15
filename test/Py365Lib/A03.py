#!/usr/bin/env python3
from Py365Lib import Common

# コマンドを実行して終了コードを確認する。(パラメータは配列であることに注意)
cmd = ["mkdir", "./testA03"]
rc = Common.exec(cmd)
print("戻り値 {0:d}".format(rc))
cmd[0] = "rmdir"
rc = Common.exec(cmd)
print("戻り値 {0:d}".format(rc))

# コマンドを実行してコマンド出力文字列を表示する。(パラメータは配列であることに注意)
cmd = ["ls", "-l", "/home/user/bin"]
b = Common.shell(cmd)
# 結果はバイト列で返されるので UTF-8 に変換する。
s = Common.from_bytes(b)
print(s)
