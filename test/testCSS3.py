#/usr/bin/env python3
# -*- coding: utf-8 -*-
#  CSS3 クラスのテスト
from Py365Lib import CSS3
import Common



# START
Common.esc_print("bold", "=== CSS3 クラスのテスト ===")
name = ""
if Common.count_args() == 0 :
  name = Common.readline("テスト名を入力する。")
  if name == "" :
    Common.stop(1, "処理を中止しました。")
else :
  name = Common.args(0)

# CSS3 オブジェクトを構築
css = CSS3.CSS3()

# テスト別の処理
if name == "preset" :
  css0 = []
  css0.append("a:link {color:dodgerblue;text-decoration:none;}")
  css0.append("a:visited {color:dodgerblue;text-decoration:none;}")
  css = CSS3.CSS3(css0)
  print(css.tostring(withtag=True))
elif name == "literal" :
  css.literal('div {margin-left:5%;border:gray thin solid;}')
  print(css.tostring(withtag=True))
elif name == "append" :
  css.literal('div {margin-left:5%;border:gray thin solid;}')
  css.concat(['a {padding:5px;}'])
  print(css.tostring(withtag=True))
elif name == "save" :
  filePath = '/home/user/testCSS3.css'
  css.literal('div {margin-left:5%;border:gray thin solid;}')
  css.save(filePath, withtag=True)
  Common.printFile(filePath)
elif name == "box_shadow" :
  css.begin_object('div', '#', 'box1')
  css.box_shadow([10, 10, 12, 12], "#8080c0")
  css.box_shadow([15, 15, 12, 12], "#c04040", True)
  css.end_object()
  print(css.tostring())
elif name == "text_shadow" :
  css.begin_object('h1')
  css.text_shadow([10, 10])
  css.text_shadow([15, 15], color="gray")
  css.text_shadow([18, 18], radius=10, color="gray")
  css.end_object()
  print(css.tostring())
elif name == "border" :
  css.begin_object('img', "class", "stamp")
  css.border(color="red")
  css.border(width="1px", style="dotted")
  css.end_object()
  print(css.tostring())
elif name == "border_radius" :
  css.begin_object('img', ".", "stamp")
  css.border_radius("10px")
  css.end_object()
  print(css.tostring())
elif name == "outline" :
  pass
elif name == "liner_gradation" :
  pass
elif name == "radial_gradation" :
  pass
elif name == "image" :
  pass
elif name == "transform" :
  pass
elif name == "rotate" :
  pass
else :
  Common.stop(9, "不正なテスト名です。")

print("終了。")
