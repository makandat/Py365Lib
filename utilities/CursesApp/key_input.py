#!/usr/bin/python3
#   表示属性
from CursesApp import CursesApp
import curses

class Application(CursesApp) :
  # コンストラクタ
  def __init__(self) :
    super().__init__()

  # オーバーライド：初期表示
  def init_app(self) :
    self.titlebar("キー入力", 1, 14)
    self.statusbar("Enter で終了", 8)
    self.print("Enter 以外のキーを押します。", 20, 4)

  # キー入力ハンドラ
  def handler(self, key) :
    self.print(str(key) + " " * 14, 25, 6, 6)
    return not (key == '\n')

# インスタンス化して実行開始
Application()
