#!/usr/bin/python3

from Py365Lib import CursesApp as cap
import curses

class Application(cap.CursesApp) :

  # オーバーライド：初期表示
  def init_app(self) :
    x = int(self.Columns / 2) - 6
    y = int(self.Rows / 2) - 1
    self.print("Hello, world!", x, y, Application.COL_GREEN)
    self.print("'q': Quit.", x, y + 1)
    return;

  # オーバーライド : キー入力ハンドラ
  def handler(self, key) :
    rc = True
    if key == 'q' :
      rc = False
    return rc
        
# インスタンス化して実行開始
Application()

