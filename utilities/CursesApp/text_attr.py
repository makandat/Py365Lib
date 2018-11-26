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
    self.titlebar("テキストの表示属性", 1, 26)
    self.statusbar("Ready", 8)
    self.print("A_BOLD (" + hex(curses.A_BOLD) + ")", 20, 3, 1, curses.A_BOLD)
    self.print("A_DIM (" + hex(curses.A_DIM) + ")", 20, 4, 1, curses.A_DIM)
    self.print("A_BLINK (" + hex(curses.A_BLINK) + ")", 20, 5, 1, curses.A_BLINK)
    self.print("A_UNDERLINE (" + hex(curses.A_UNDERLINE) + ")", 20, 6, 1, curses.A_UNDERLINE)
    self.print("A_NORMAL (" + hex(curses.A_NORMAL) + ")", 20, 7, 1, curses.A_NORMAL)
    self.print("A_REVERSE (" + hex(curses.A_REVERSE) + ")", 20, 8, 1, curses.A_REVERSE)
    self.print("A_UNDERLINE + color_pair(4) (" + hex(curses.A_UNDERLINE + curses.color_pair(4)) + ")", 20, 9, 1, curses.A_UNDERLINE + curses.color_pair(4))
    self.hideCursor()

# インスタンス化して実行開始
Application()
