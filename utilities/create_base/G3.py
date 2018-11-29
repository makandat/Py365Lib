#  注意　"python3 test_TkApp3.py" として実行すること。 
import sys
import TkApp as tkapp
import tkinter as tk

# TkApp から継承するクラス
class TkApp3(tkapp.TkApp) :
  count = 0

  def __init__(self, parent, winprop, deffile) :
    super().__init__(parent, winprop, deffile)
    self.commands["button1"] = self.button1_click
    self.setCommands()

  def button1_click(self) :
    self.setWidget("label1", "text", "button1_click " + str(self.count))
    self.count += 1
    return

# widget 定義ファイル名を決める。
deffile = sys.argv[0].replace('.py', '.json')

# root を作る。グローバル変数 "root" は存在する必要がある。
root = tk.Tk()
# Application を作る。
winprop = {"title":"TkApp3", "left":100, "top":100, "width":512, "height":320}
app = TkApp3(root, winprop, deffile)
# イベントループに入る。
app.mainloop()

