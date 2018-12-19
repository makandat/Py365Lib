#!/usr/bin/python3
from Py365Lib import CursesApp as cap
import curses

## アプリケーションクラス
class Application(cap.CursesApp) :

  # 画面初期表示
  def init_app(self) :
    self.titlebar("色の作成", Application.TB_ALIGN_CENTER, Application.REV_WHITE)
    self.statusbar("q: Quit", Application.REV_WHITE)
    self.redraw()
    self.hideCursor()
    return

  # 再描画
  def redraw(self) :
    self.print("Color Pair = 33", 25, 3, 33)
    self.print("Color Pair = 34", 25, 4, 34)
    self.print("Color Pair = 35", 25, 5, 35)
    self.print("Color Pair = 36", 25, 6, 36)
    self.print("Color Pair = 37", 25, 7, 37)
    self.print("Color Pair = 38", 25, 8, 38)
    return

  # カラーペア初期化
  def init_colors(self) :
    super().init_colors()
    self.setColor(33, curses.COLOR_BLUE, curses.COLOR_GREEN)
    self.setColor(34, curses.COLOR_RED, curses.COLOR_GREEN)
    self.setColor(35, curses.COLOR_YELLOW, curses.COLOR_GREEN)
    self.setColor(36, curses.COLOR_RED, curses.COLOR_BLUE)
    self.setColor(37, curses.COLOR_GREEN , curses.COLOR_BLUE)
    self.setColor(38, curses.COLOR_YELLOW , curses.COLOR_BLUE)
    return

  # キー入力ハンドラ
  def handler(self, key) :
    rc = True
    if key == 'q' :
      rc = False
    return rc

# アプリケーションをインスタンス化して開始
Application()
