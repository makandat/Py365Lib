#
#  curses アプリケーションクラス
#     Version 1.11 2018-12-06
#
import curses
import os, locale
import math
import unicodedata
import json
from syslog import syslog

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
  # 文字コード
  LF  = '\x0a'
  TAB = '\x09'
  ESC = '\x1b'

  # フォームのコレクション
  forms = {}
  #  ラジオボタングループ
  group = []
  # 選択されたフォーム
  selectedForm = None
  # 現在のタブインデックス
  tabidx = 0
  # フォームデータ (OKのとき)
  formData = {}

  # コンストラクタ
  def __init__(self) :
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
    while True :
      c = self.stdscr.getkey()
      if self.handler(c) == False:
        break

  # キー入力ハンドラ (オーバーライドが必要)
  def handler(self, key) :
    return False

  # 初期表示を行う。 (オーバーライドが必要)
  def init_app(self) :
    self.stdscr.addstr("     ERROR: init_app() and handler() should be overriden.")

  # 再描画する。 (初期表示と異なる場合はオーバーライドが必要)
  def redraw(self) :
    self.clear()
    self.init_app()

  # 構成ファイル AppConf.ini を読み込んで self.conf に内容を保存
  def readConf(self) :
    self.conf = {}
    if not os.path.exists(CursesApp.APPCONF) :
      return
    with open(CursesApp.APPCONF) as f :
      for line in f :
        if line[0] == '#' or line[0] == '[' or len(line) == 0:
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
      tj = CursesApp.left_justify(text, self.Columns - 1)
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
    tj = CursesApp.left_justify(text, self.Columns - 1)
    if color > 0 :
      self.stdscr.addstr(self.Rows - 1, 0, tj, curses.color_pair(color))
    else :
      self.stdscr.addstr(self.Rows - 1, 0, tj)

  # 文字列を表示する。
  def print(self, str, x = -1, y = -1, color = -1, attr = 0) :
    if x >= 0 and y >= 0 :
      if y >= self.Rows :
        return
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

  # 改行を含む文字列を表示する。(text は文字列または文字列配列)
  def printLines(self, text, x, y, color=1, attr=0) :
    if type(text) is str :
      lines = text.split('\n')
    else :
      lines = text
    for l in lines :
      self.stdscr.addstr(y, x, l, curses.color_pair(color) + attr)
      y += 1
      if y >= (self.Rows - 1):
        break
    return

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
    (y, x) = self.stdscr.getyx()
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
    start = 0
    helpw = curses.newwin(self.Rows - 2, self.Columns, 1, 0)
    self.__showHelp(helpw, text, title, start)
    # キーが押されるまでループ
    while True :
      key = helpw.getkey()
      if str(key) == 'KEY_DOWN' :
        start += (self.Columns - 2)
        self.__showHelp(text, title, start)
      elif str(key) == 'KEY_UP' :
        start -= (self.Columns - 2)
        if start < 0 :
          start = 0
        self.__showHelp(text, title, start)
      elif str(key) == 'KEY_HOME' :
        start = 0
        self.__showHelp(text, title, start)
      else :
        break
    return

  # ヘルプを表示する。
  def __showHelp(self, helpw, text, title="", start=0) :
    helpw.clear()
    y = 1
    x = 0
    if title != "" :
      title_text = CursesApp.center_justify(title, self.Columns)
      helpw.addstr(y, 0, title_text, curses.color_pair(3))
      y += 1
    lines = text.split('\n')
    i = start
    while (y <= self.Rows - 1) and (i < len(lines)) :
      line = lines[i]
      helpw.addstr(y, 0, line)
      y += 1
      i += 1
    return

  # フォームを作成して登録する。(表示はしない) data は json 形式テキスト
  def createForm(self, name, data) :
    widgets = json.loads(data)
    # フォームを登録する。
    self.forms[name] = widgets
    return

  # フォームを切り替える。(表示する)
  def selectForm(self, name) :
    self.tabidx = 0
    self.selectedForm = name
    self.clear(True)  # クライアント領域のみクリア
    self.formData = {}
    self.drawWidgets(name)
    self.tabidx = self.selectWidget()   
    return

  # name で指定されたフォームのウィジェットを描画する。
  def drawWidgets(self, name) :
    # フォームの描画先を決定
    form = self.stdscr
    # ウィジェットリストを取得
    widgets = self.forms[name]
    # それぞれのウィジェットについて描画する。
    self.group = []
    for w in widgets :
      if w["type"] == 'label' :
        text = w["text"]
        self.formData[w['name']] = text
        if "width" in w and w["width"] > 0 :
          text = CursesApp.center_justify(text, w["width"])
        if "color" in w.keys() :
          form.addstr(w["top"], w["left"], text, curses.color_pair(w["color"]))
          if "attr" in w.keys() :
            form.addstr(w["top"], w["left"], text, curses.color_pair(w["color"]) + w["attr"])
        else :
          form.addstr(w["top"], w["left"], text, curses.color_pair(1))              
      elif w["type"] == 'button' :
        self.formData[w['name']] = str(w['click'])
        if "color" in w.keys() :
          form.addstr(w["top"], w["left"], "  " + w["text"] + "  ", curses.color_pair(w["color"]))
        else :
          form.addstr(w["top"], w["left"], "  " + w["text"] + "  ", curses.color_pair(8))
      elif w["type"] == 'textbox' or w["type"] == "text":
        self.formData[w['name']] = ""
        cpair = curses.color_pair(8)
        if "color" in w.keys() :
          cpair = curses.color_pair(w["color"])
        textw = 15
        if "width" in w.keys() :
          textw = w["width"]
        form.addstr(w["top"], w["left"], " " * textw, cpair)
        if "text" in w.keys() and w["text"] != "" :
          form.addstr(w["top"], w["left"], w["text"], cpair)
      elif w["type"] == 'checkbox' :
        check = "["
        if w["checked"] :
          check += "X] "
          self.formData[w['name']] = "True"
        else :
          self.formData[w['name']] = "False"
          check += " ] "       
        check += w["text"]
        form.addstr(w["top"], w["left"], check)
      elif w["type"] == 'radio' :
        check = "["
        if w["checked"] :
          check += "O] "
          self.formData[w['name']] = "True"
        else :
          self.formData[w['name']] = "False"
          check += " ] "
        check += " "
        check += w["text"]
        self.group.append({"name":w['name'], "x":w["left"], "y":w["top"], "checked":w["checked"]})
        form.addstr(w["top"], w["left"], check)
      elif w["type"] == 'selector' :
        self.formData[w['name']] = "0"
        items = w["items"]
        cpair = curses.color_pair(1)
        if "color" in w.keys() :
          cpair = curses.color_pair(w["color"])
        form.addstr(w["top"], w["left"], items[0], cpair + curses.A_REVERSE)
        n = len(items)
        for i in range(1, n) :
           form.addstr(w["top"] + i, w["left"], items[i], cpair)
      else :
        pass
    return

  # ウィジェットのプロパティを変更する。
  def setProperty(self, form, name, key, value) :
     widgets = self.forms[form]
     for w in widgets :
        if w["name"] == name :
          w[key] = value
          self.drawWidgets(form)
     return

  # ウィジェットのプロパティを得る。
  def getProperty(self, form, name, key) :
     prop = None
     widgets = self.forms[form]
     for w in widgets :
        if w["name"] == name :
          prop = w[key]
     return prop

  # ラベルのテキストを得る。
  def getLabel(self, name) :
     return self.getProperty(self.selectedForm, name, "text")

  # ラベルのテキストを変更する。
  def setLabel(self, name, text) :
     self.setProperty(self.selectedForm, name, "text", text)
     return
     
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

  # 入力ボックスを開く
  def inputBox(self, message) :
    width = 50
    x = math.floor((self.Columns - width) / 2)
    y = 5
    win = curses.newwin(4, width, y, x)
    win.border()
    win.addstr(1, 1, message)
    curses.curs_set(1)
    curses.echo()
    win.refresh()
    data = win.getstr(2, 1, (width - 3))
    s = data.decode('utf-8')
    return s

  # 指定した秒数だけ文字列を表示する。
  def toast(self, message, seconds=2, color=2) :
    width = math.floor(self.Columns / 2)
    x = math.floor((self.Columns - width) / 2)
    y = math.floor(self.Rows / 2) - 1
    win = curses.newwin(1, width, y, x)
    win.addstr(0, 0, ' ' + message + ' ', curses.color_pair(color) + curses.A_BLINK)
    win.refresh()
    curses.napms(int(1000.0 * seconds))
    self.redraw()
    return

  # 次の有効なウィジェットの位置(tabidx)を得る。
  def selectWidget(self) :
    # 対象のフォームを特定する。
    if self.selectedForm == None :
      return -1
    form = self.forms[self.selectedForm]
    # フォームにラベルのみしかないか判別
    for i in range(len(form)) :
      w = form[i]
      if w['type'] != 'label' :
        break
    if i == len(form) - 1 :
      return -1
    # 次のウィジェットへ
    idx = self.tabidx + 1
    if idx >= len(form) :
      idx = 0
    # 現在のウィジェットを特定する。
    widget = form[idx]
    # ウィジェットがラベルなら次へ
    while widget['type'] == 'label' :
      idx += 1
      if idx >= len(form) :
        idx = 0
      widget = form[idx]
    return idx

  # 指定したウィジェットへカーソルを移動する。
  def setCursorToWidget(self, widget) :
    self.showCursor()
    if widget['type'] == 'radio' or widget['type'] == 'checkbox' :
      self.setCursorPosition(widget['left'] + 1, widget['top'])
    elif widget['type'] == 'button' :
      if "width" in widget.keys() :
        p = int(widget['width'] / 2)
      else:
        p = 2
      self.setCursorPosition(widget['left'] + p, widget['top'])
    else :
      self.setCursorPosition(widget['left'], widget['top'])

  # キー入力
  def enterText(self, widget) :
    if widget['type'] == 'textbox' or widget['type'] == 'text':
      curses.echo()
      if "width" in widget.keys() :
        s = self.stdscr.getstr(widget['width'] - 1).decode('utf-8').strip()
      else :
        s = self.stdscr.getstr(14).decode('utf-8').strip()
      curses.noecho()
      self.stdscr.addstr(widget['top'], widget['left'], s, curses.A_REVERSE)
      self.formData[widget['name']] = s
      self.tabidx += 1
      return s
    else :
      return ''

  # チェックボックス、ラジオボタン　空白キー
  def changeChecked(self, widget, form) :
    if widget['type'] == 'checkbox' :  # チェックボックス
      if widget['checked'] :
        self.stdscr.addch(' ')
        self.formData[widget['name']] = "True"
        self.setCursorPosition(widget['left'] + 1, widget['top'])
      else :
        self.stdscr.addch('X')
        self.formData[widget['name']] = "False"
        self.setCursorPosition(widget['left'] + 1, widget['top'])
    elif widget['type'] == 'radio' :  # ラジオボタン
      # グループをいったんクリア
      for w in form :
        if w['type'] == 'radio' :
          w['checked'] = False
      for w in self.group :
        self.formData[w['name']] = "False"
        # このラジオボタンを選択状態にする。
        if w['name'] == widget['name'] :
          w['checked'] = True
          self.formData[widget['name']] = "True"
          self.stdscr.addch(widget['top'], widget['left'] + 1, 'O')
        else :
          self.stdscr.addch(w['y'], w['x'] + 1, ' ')
          w['checked'] = False
      self.setCursorPosition(widget['left'] + 1, widget['top'])
    else :
      pass

  # セレクタ UP キー
  def selectUp(self, widget) :
    if widget['type'] == 'selector' :
      # selected プロパティが 0 なら何もしない。
      if widget["selected"] == 0 :
        return
      widget["selected"] -= 1
      x = widget['left']
      y = widget['top']
      items = widget['items']
      for i in range(len(items)) :
        if i == widget['selected'] :
          self.stdscr.addstr(y, x, items[i], curses.A_REVERSE)
          self.formData[widget['name']] = str(i)
        else :
          self.stdscr.addstr(y, x, items[i])
        y += 1
    return

  # セレクタ DOWN キー
  def selectDown(self, widget) :
    if widget['type'] == 'selector' :
      x = widget['left']
      y = widget['top']
      items = widget['items']
      # selected プロパティが 項目数-1 なら何もしない。
      if widget["selected"] == (len(items) - 1) :
        return
      widget["selected"] += 1
      for i in range(len(items)) :
        if i == widget['selected'] :
          self.stdscr.addstr(y, x, items[i], curses.A_REVERSE)
          self.formData[widget['name']] = str(i)
        else :
          self.stdscr.addstr(y, x, items[i])
        y += 1
    return

  # ボタンが押されたとき
  def buttonPressed(self, widget) :
    if widget['type'] == 'button' :
      cpair = 8
      if "color" in widget.keys() :
        cpair = curses.color_pair(widget['color'])
      self.stdscr.addstr(widget['top'], widget['left'], " " + widget['text'] + " ", cpair + curses.A_REVERSE)
      self.stdscr.refresh()
      curses.napms(300)
      self.stdscr.addstr(widget['top'], widget['left'], " " + widget['text'] + " ", cpair)
      self.stdscr.refresh()
      return widget['click']
    else :
      return -1


  # アラート
  def alert(self, message) :
    self.statusbar(message)
    curses.flash()

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

  # フォームのウィジェット定義を読んでフォームを構築する。
  def readFormData(self, name, fileName) :
    data = None
    with open(fileName) as f :
      str = f.read()
      self.createForm(name, str)
    return 
