#!/usr/bin/python3
from Py365Lib import CursesApp as cap
import curses

## アプリケーションクラス
class Application(cap.CursesApp) :
  # 画面初期化
  def init_app(self) :
    self.redraw()
    self.hideCursor()
    return

  # 再描画
  def redraw(self) :
    self.titlebar("Title bar", Application.TB_ALIGN_CENTER, Application.REV_CYAN)
    self.statusbar("Status bar", Application.REV_CYAN)
    x = int((self.Columns - 5) / 2)
    y = int(self.Rows / 2)
    self.print("Hello", x, y, 5)
    return

  # キー入力ハンドラ
  def handler(self, key) :
    rc = True
    if key == 'q' :
      rc = False
    return rc


# アプリケーションをインスタンス化して開始
Application()

