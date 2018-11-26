#
#  curses アプリケーションクラス
#     ver 0.61 2018-10-14
#     ver 1.00 2018-10-29
#
import curses
import os, locale
import math
import unicodedata

#  アプリケーションクラス
class CursesApp :
  APPCONF = "AppConf.ini"
  # 表示属性
  UNDERLINE = curses.A_UNDERLINE
  BLINK = curses.A_BLINK
  BOLD = curses.A_BOLD
  REVERSE = curses.A_REVERSE
  DIM = curses.A_DIM
  NORMAL = curses.A_NORMAL
  # タイトルバーのテキスト表示位置
  TB_ALIGN_LEFT = 0
  TB_ALIGN_CENTER = 1
  # メッセージボックスの指定
  MB_OKONLY = 0
  MB_YESNO = 1
  MB_OKCANCEL = 2
  # ボタン
  BTN_OK = 0
  BTN_CANCEL = 1
     
  # コンストラクタ
  def __init__(self, main_loop=True) :
    # メインループに入るかどうか
    self.main_loop = main_loop
    # フォームのコレクション
    self.forms = []
    # 構成ファイルが存在する場合、それを読んで構成データを初期化する。
    self.readConf()
    # ロケールの設定
    locale.setlocale(locale.LC_ALL, '')
    self.code = locale.getpreferredencoding()  # str.encode(code) で使用する。
    # 初期化する。
    self.stdscr = curses.initscr()
    curses.start_color()
    # キーのエコーを行わない。
    curses.noecho()
    # キー入力のバッファリングをしない。
    curses.cbreak()
    # 制御キーを扱えるようにする。
    self.stdscr.keypad(True)
    # カラーペアを初期化
    self.init_colors()
    try :
        # 初期表示
        self.init_app()
        # ループ
        self.main()
    finally :
        # 後始末を行う。
        self.end_app()

  # 後始末（デフォルトで終了時に呼び出される）
  def end_app(self) :
    # キー入力をバッファリングする。
    curses.nocbreak()
    # 制御キーを扱わない。
    self.stdscr.keypad(False)
    curses.echo()
    # 端末を通常モードに復旧する。
    curses.endwin()

  # キー入力ループ
  def main(self) :
    while self.main_loop :
      c = self.stdscr.getkey()
      if not self.handler(c) :
        break

  # キー入力ハンドラ (オーバーライドが必要)
  def handler(self, key) :
    return False

  # 初期表示を行う。 (オーバーライドが必要)
  def init_app(self) :
    self.stdscr.addstr("init_app() and handler() should be overriden.")

  # 再描画する。 (オーバーライドが必要な場合がある)
  def redraw(self) :
    self.clear()
    self.init_app()
    self.main_loop = True

  # 構成ファイル AppConf.ini を読み込んで self.conf に内容を保存
  def readConf(self) :
    self.conf = {}
    if not os.path.exists(CursesApp.APPCONF) :
      return
    with open(CursesApp.APPCONF) as f :
      for line in f :
        if line.startwith('#') or line.startwith('[') or len(line) == 0:
          continue
        kv = line.split('=')
        if len(kv) == 2 :
          key = kv[0].strip()
          value = kv[1].strip()
          self.conf[key] = value
    return

  # カラーペアを初期化
  def init_colors(self) :
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(9, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(10, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(11, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(12, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(13, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
    curses.init_pair(14, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(15, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(16, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(17, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(18, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(19, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(20, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(21, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    curses.init_pair(22, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    curses.init_pair(23, curses.COLOR_WHITE, curses.COLOR_CYAN)
    curses.init_pair(24, curses.COLOR_CYAN, curses.COLOR_WHITE)
    curses.init_pair(25, curses.COLOR_CYAN, curses.COLOR_YELLOW)
    curses.init_pair(26, curses.COLOR_CYAN, curses.COLOR_BLUE)
    curses.init_pair(27, curses.COLOR_YELLOW, curses.COLOR_BLUE)
    curses.init_pair(28, curses.COLOR_RED, curses.COLOR_GREEN)
    curses.init_pair(29, curses.COLOR_GREEN, curses.COLOR_RED)
    curses.init_pair(30, curses.COLOR_RED, curses.COLOR_YELLOW)
    curses.init_pair(31, curses.COLOR_YELLOW, curses.COLOR_RED)
    curses.init_pair(32, curses.COLOR_CYAN, curses.COLOR_MAGENTA)

  # タイトルバーを表示する。
  def titlebar(self, text, align=0, color=-1) :
    if align == 0 :
      tj = CursesApp.left_justify(text, self.Columns)
    elif align == 1 :
      tj = CursesApp.center_justify(text, self.Columns)
    else :
      return
    if color > 0 :
      self.stdscr.addstr(0, 0, tj, curses.color_pair(color) + curses.A_BOLD)
    else :
      self.stdscr.addstr(0, 0, tj, curses.A_BOLD)

  # ステータスバーを表示する。
  def statusbar(self, text, color=-1) :
    tj = CursesApp.left_justify(text, self.Columns)
    if color > 0 :
      self.stdscr.addstr(self.Rows - 1, 0, tj, curses.color_pair(color))
    else :
      self.stdscr.addstr(self.Rows - 1, 0, tj)

  # 文字列を表示する。
  def print(self, str, x = -1, y = -1, color = -1, attr = 0) :
    if x >= 0 and y >= 0 :
      if color >= 0 :
        self.stdscr.addstr(y, x, str, curses.color_pair(color) + attr)
      else :
        self.stdscr.addstr(y, x, str)
    else :
      if color >= 0 :
        self.stdscr.addstr(str, curses.color_pair(color) + attr)
      else :
        self.stdscr.addstr(str)
    self.stdscr.refresh()

  # 改行を含む文字列を表示する。
  def printLines(text, start=0, color=-1, attr=0) :
    lines = text.split('\n')
    (x, y) = self.getCursorPosition()
    for i in range(start, len(lines)) :
      self.stdscr.addstr(y, x, lines[i])
      y += 1

  # 座標を指定して文字を表示する。
  def putchar(self, ch, x = -1, y = -1) :
    x = 0 if x < 0 else x
    y = 0 if y < 0 else y
    self.stdscr.addch(y, x, ch)

  # 文字を表示する。
  def putch(self, ch) :
    y, x = curses.getsyx()
    self.stdscr.addch(y, x, ch)

  # カーソルの座標を移動する。
  def setCursorPosition(self, x, y) :
    self.stdscr.move(y, x)

  # カーソルの位置を得る。
  def getCursorPosition(self) :
    (y, x) = curses.getsyx()
    return (x, y)

  # カーソルを非表示にする。
  def hideCursor(self) :
    curses.curs_set(0)

  # カーソルを表示する。
  def showCursor(self) :
    curses.curs_set(1)

  # 色対番号を追加または変更
  def setColor(self, n, foreground, background) :
    if n >= 1 and n <= curses.COLOR_PAIRS :
      curses.init_pair(n, foreground, background)

  # 色を新しく作る。
  def makeColor(self, n, r, g, b) :
    if n >= 0 and n <= curses.COLORS :
      curses.init_color(n. r, g, b)

  # ウィンドウのカラム数
  @property
  def Columns(self) :
    tup = self.stdscr.getmaxyx()
    return tup[1]

  # ウィンドウの行数
  @property
  def Rows(self) :
    tup = self.stdscr.getmaxyx()
    return tup[0]

  # 最大の色番号
  @property
  def MaxColorNumber(self) :
    return curses.COLOR_PAIRS - 1

  # 画面をクリアする。
  def clear(self, client=False) :
    if client :
      s = " " * self.Columns
      for i in range(self.Rows - 2) :
        self.stdscr.addstr(i + 1, 0, s)
    else :
      self.stdscr.clear()

  # 画面に属性をセットする。属性は curses.A_BLINK などである。
  def setAttr(self, attr) :
    self.stdscr.attrset(attr)

  # 指定した属性をオフにする。
  def setAttrOff(self, attr) :
    self.stdscr.attroff(attr)

  # 指定した属性をオンにする。
  def setAttrOn(self, attr) :
    self.stdscr.attron(attr)

  # ヘルプウィンドウを開く
  def helpWindow(self, text, title="") :
    y = 1
    x = 0
    helpw = curses.newwin(self.Rows - 2, self.Columns, 1, 0)
    if title != "" :
      title_text = CursesApp.center_justify(title, self.Columns)
      helpw.addstr(y, 0, title_text, curses.color_pair(3))
      y += 1
    lines = text.split('\n')
    for line in lines :
      helpw.addstr(y, 0, line)
      y += 1
    # キーが押されるまでループ
    while True :
      helpw.getkey()
      break
    return

        
  # フォームを作成する。
  def createForm(self, json) :
    pass

  # メッセージボックスを開く
  def messageBox(self, message, type=0) :
    value = CursesApp.BTN_OK  # OK
    width = 50
    height = 12
    x_ok = 20
    y_ok = 10
    x = math.floor((self.Columns - width) / 2)
    y = math.floor((self.Rows - height) / 2)
    msgbox = curses.newwin(height, width, y, x)
    msgbox.border()
    msgbox.addstr(3, 1, message)
    if type == CursesApp.MB_YESNO :
      msgbox.addstr(y_ok, x_ok, "   Yes  ", curses.color_pair(8))
      msgbox.addstr(y_ok, x_ok + 12, "   No   ", curses.color_pair(8))
      msgbox.move(y_ok, x_ok)
    elif type == CursesApp.MB_OKCANCEL :
      msgbox.addstr(y_ok, x_ok, "   OK   ", curses.color_pair(8))
      msgbox.addstr(y_ok, x_ok + 12, " Cancel ", curses.color_pair(8))
      msgbox.move(y_ok, x_ok)
    else :  # MB_OKONLY
      msgbox.addstr(10, 33, "  OK  ", curses.color_pair(8))
      msgbox.move(10, 33)
    self.showCursor()
    # キー入力待ち
    while True :
      key = msgbox.getkey()
      if key == '\n' :
        break
      elif key == '\t' :
        if value == CursesApp.BTN_OK :
          msgbox.move(y_ok, x_ok + 12)
          value = CursesApp.BTN_CANCEL
        else :
          msgbox.move(y_ok, x_ok)
          value = CursesApp.BTN_OK
      elif ord(key) == 0x1b :
        value = CursesApp.BTN_CANCEL
        break
      else :
        pass
    self.hideCursor()
    return value

  @staticmethod
  def left_justify(text, width) :
    # 全角１文字2文字として文字数を求める。
    n = 0
    for c in text :
      s = unicodedata.east_asian_width(c)
      if s == "W" or s == "F" :  # 全角の場合
        n += 2
      else :
        n += 1
    # 半角空白を追加する。
    n2 = width - n - 1
    text2 = text + " " * n2
    return text2

  @staticmethod
  def center_justify(text, width) :
    # 全角１文字2文字として文字数を求める。
    n = 0
    for c in text :
      s = unicodedata.east_asian_width(c)
      if s == "W" or s == "F" :  # 全角の場合
        n += 2
      else :
        n += 1
    # 前に半角空白を追加する。
    n2 = math.floor((width - n) / 2)
    text2 = " " * n2 + text
    # 後ろに半角空白を追加する。
    text2 = text2 + " " * n2
    return text2
