#  TkApp5.py
# -*- coding: utf-8 -*-
import sys
import TkApp as tkapp
import tkinter as tk


# TkApp から継承するクラス
class TkApp5(tkapp.TkApp) :

  # コンストラクタ
  def __init__(self, parent, winprop, deffile) :
    super().__init__(parent, winprop, deffile)
    self.commands["mnuOpen_Click"] = self.mnuOpen_Click
    self.commands["mnuQuit_Click"] = root.destroy
    self.commands["mnuAbout_Click"] = self.mnuAbout_Click
    self.setCommands()

  # Open メニューハンドラ
  def mnuOpen_Click(self) :
    w = self.getWidget('label1')
    w['text'] = "mnuOpen_Click"
    return

  # Help メニューハンドラ
  def mnuAbout_Click(self) :
    w = self.getWidget('label1')
    w['text'] = "mnuAbout_Click"
    return


# widget 定義ファイル名を決める。
deffile = sys.argv[0].replace('.py', '.json')

# root を作る。グローバル変数 "root" は存在する必要がある。
root = tk.Tk()
# Application を作る。
winprop = {"title":"TkApp5", "left":100, "top":100, "width":512, "height":320}
app = TkApp5(root, winprop, deffile)
# イベントループに入る。
app.mainloop()

