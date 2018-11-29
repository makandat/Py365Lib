#  注意　"python3 test_TkApp2.py" として実行すること。 
import sys
import TkApp as tkapp
import tkinter as tk


# widget 定義ファイル名を決める。
deffile = sys.argv[0].replace('.py', '.json')

# root を作る。グローバル変数 "root" は存在する必要がある。
root = tk.Tk()
# Application を作る。
winprop = {"title":"TkApp2", "left":100, "top":100, "width":512, "height":320, "fixedborder":False}
app = tkapp.TkApp(root, winprop, deffile)
# イベントループに入る。
app.mainloop()

