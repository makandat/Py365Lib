#  TkApp6.py
# -*- coding: utf-8 -*-
import sys
import TkApp as tkapp
import tkinter as tk


# TkApp から継承するクラス
class TkApp6(tkapp.TkApp) :

  # コンストラクタ
  def __init__(self, parent, winprop, deffile) :
    super().__init__(parent, winprop, deffile)
    self.commands["button1"] = self.button1_click
    self.commands["button2"] = root.destroy
    self.setCommands()

  def button1_click(self) :
    message = "text1="
    message += self.getWidgetValue('text1')
    message += ", text2="
    message += self.getWidgetValue('text2')
    message += ", list1="
    message += str(self.getWidgetValue('list1'))
    message += ", check1="
    message += str(self.getWidgetValue('check1'))
    self.setWidget("statusbar", "text", "radio: " + str(self.radioval.get()))
    self.messageBox(message, "info")

# widget 定義ファイル名を決める。
deffile = sys.argv[0].replace('.py', '.json')

# root を作る。グローバル変数 "root" は存在する必要がある。
root = tk.Tk()
# Application を作る。
winprop = {"title":"TkApp6", "left":100, "top":100, "width":512, "height":320}
app = TkApp6(root, winprop, deffile)
# イベントループに入る。
app.mainloop()
