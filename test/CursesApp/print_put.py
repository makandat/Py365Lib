#!/usr/bin/python3
from Py365Lib import CursesApp as cap
import curses

## アプリケーションクラス
class Application(cap.CursesApp) :
  thekey = '-'

  # 画面初期表示
  def init_app(self) :
    self.print("'0': putchar(), '1': putch(), '2': print(), '3': printLines(), 'q': Quit", 10, 8)
    self.hideCursor()
    self.redraw()
    return

  # 再描画
  def redraw(self) :
    if Application.thekey =='0' :
      # '0' キーが押されたとき、画面をクリアして文字をたてに表示
      self.clear()
      self.setCursorPosition(20, 1)
      i = 0
      for a in range(ord('0'), ord(':')) :
        self.putchar(chr(a), 20, i + 1)
        i += 1
    elif Application.thekey == '1' :
      # '1' キーが押されたとき、キーを１回押すごとに 'X' を横に表示
      self.putch('X')
    elif Application.thekey == '2' :
      # '2' キーが押されたとき、画面をクリアして文字列 'self.print()' を Magenta のボールドで表示
      self.clear()
      self.print("self.print()", 10, 5, Application.COL_MAGENTA, Application.BOLD)
    elif Application.thekey == '3' :
      # '3' キーが押されたとき、画面をクリアして改行を含む文字列を黄色で表示
      self.clear()
      self.printLines('''printLines
    printLines
            printLines
''',
      10, 5, Application.COL_YELLOW)
    else :
      pass
    return

  # キー入力ハンドラ
  def handler(self, key) :
    rc = True
    if key == 'q' :
      rc = False
    elif key == '0' or key == '1' or key == '2' or key == '3' :
      Application.thekey = key
      self.redraw()
    else :
      pass
    return rc

# アプリケーションをインスタンス化して開始
Application()

