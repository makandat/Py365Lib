#  注意　"python3 test_TkApp4.py" として実行すること。 
import sys
import TkApp as tkapp
import tkinter as tk

# TkApp から継承するクラス
class TkApp4(tkapp.TkApp) :
  count = 0

  def __init__(self, parent, winprop, deffile) :
    super().__init__(parent, winprop, deffile)

# widget 定義ファイル名を決める。
deffile = sys.argv[0].replace('.py', '.json')

# root を作る。グローバル変数 "root" は存在する必要がある。
root = tk.Tk()
# Application を作る。
winprop = {"title":"TkApp4", "left":100, "top":100, "width":512, "height":320}
app = TkApp4(root, winprop, deffile)
# イベントループに入る。
app.mainloop()

