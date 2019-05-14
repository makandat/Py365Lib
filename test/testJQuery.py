#/usr/bin/env python3
# -*- coding: utf-8 -*-
#  JQuery クラスのテスト
from Py365Lib import JQuery, Common


# START
Common.esc_print("bold", "=== CSS3 クラスのテスト ===")
name = ""
if Common.count_args() == 0 :
  name = Common.readline("テスト名を入力する。")
else :
  name = Common.args(0)

# JQuery オブジェクトを構築
jq = JQuery()

# テスト別の処理
if name == "" :

else :
  Common.stop(9, "不正なテスト名です。")

print("終了。")

