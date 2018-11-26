#!/usr/bin/python3

from CursesApp import CursesApp
import curses

class Application(CursesApp) :
  cls = False

  # コンストラクタ
  def __init__(self) :
    super().__init__()

  # オーバーライド：初期表示
  def init_app(self) :
    self.setColor(18, curses.COLOR_WHITE, curses.COLOR_RED)
    self.print("Columns = " + str(self.Columns) + " Rows = " + str(self.Rows), 4, 1, 18)
    self.print("'q': 終了", 8, 3, 5)
    self.print("'c': 画面クリア ON / OFF", 8, 4, 5)
    self.print("'h': カーソルを表示しない", 8, 5, 5)
    self.print("'i': カーソルを表示する", 8, 6, 5)
    self.print("'m': カーソルを (x:6, y:12) へ移動する", 8, 7, 5)
    self.print("'a': 属性をセットする (TeraTerm 不可)", 8, 8, 5)
    self.print("'o': 属性を OFF する", 8, 9, 5)
    self.print("'n': 属性を ON する", 8, 10, 5)

  # オーバーライド : キー入力ハンドラ
  def handler(self, key) :
    rc = True
    if key == 'c' : # 画面クリア
        if self.cls == False :
          self.clear()
          self.cls = True
        else :
          self.init_app()
          self.cls = False
    elif key == 'h' : # カーソルを表示しない
        self.hideCursor()
    elif key == 'i' : # カーソルを表示する
        self.showCursor()
    elif key == 'm' : # カーソルを移動する
        self.setCursorPosition(6, 12)
        (x, y) = self.getCursorPosition()
        self.stdscr.addstr(y, x, str(x) + ", " + str(y))
    elif key == 'a' : # 属性をセットする
        self.setAttr(curses.A_BLINK)
        self.stdscr.addstr(13, 6, 'curses.A_BLINK')
    elif key == 'o' : # 属性を OFF する
        self.setAttrOff(curses.A_BLINK)
        self.stdscr.addstr(13, 6, 'curses.A_BLINK')
    elif key == 'n' : # 属性を ON する
        self.setAttrOn(curses.A_BLINK)
        self.stdscr.addstr(13, 6, 'curses.A_BLINK')
    elif key == 'q' : # アプリ終了
        rc = False
    else :
        pass
    return rc
        
# インスタンス化して実行開始
Application()

