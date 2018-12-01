#  注意　"python3 G0.py" として実行すること。 
import sys
import FileSystem
import TkApp as tkapp
import tkinter as tk


class Tk0(tkapp.TkApp) :
    # ウィジェット作成メソッドをオーバーライド
    def createWidgets(self, filename) :
        if FileSystem.exists(filename) :
            super().createWidgets(filename)
        else :
            self.button1 = tk.Button(self, text="Button1", command=root.destroy)
            self.button1.pack()
        return

# widget 定義ファイル名を決める。
deffile = sys.argv[0].replace('.py', '.json')

# root を作る。グローバル変数 "root" は存在する必要がある。
root = tk.Tk()
# Application を作る。
winprop = {"title":"Hello", "left":100, "top":100, "width":480, "height":200, "fixedborder":True}
app = Tk0(root, winprop, deffile)
# イベントループに入る。
app.mainloop()

