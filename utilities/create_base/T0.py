#!/usr/bin/python3

from CursesApp import CursesApp
import curses

class Application(CursesApp) :
  cls = False

  # コンストラクタ
  def __init__(self) :
    super().__init__()
    return

  # オーバーライド：初期表示
  def init_app(self) :
    x = int(self.Columns / 2) - 6
    y = int(self.Rows / 2) - 1
    self.print("Hello, world!", x, y, 3)
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

