#!/usr/bin/python3
#  JSON が正しい形式化をチェックする。
from Common import *
from FileSystem import *
from pprint import pprint


# コマンド引数の確認
if count_args() == 0 :
    print(ESC_FG_RED + "JSON ファイルを指定してください。")
    print(ESC_NORMAL)
    exit(9)

# CSV ファイル
jsonfile = args()[0]

# JSON ファイルを読む。
text = FileSystem.readAllText(jsonfile)
try :
    po = from_json(text)
    pprint(po)
except :
    print("JSON エラーを検出。")
