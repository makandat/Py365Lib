#!/usr/bin/python3
from Py365Lib import CursesApp as cap

# アプリケーションクラス
class Application(cap.CursesApp) :
  # ヘルプ表示中かどうか
  helpWin = False
  # ヘルプウィンドウの表示内容
  HELP = """Help Window
  　　ここにヘルプを表示できます。
  HelpWindow

     'h' ２回で閉じる。
  """

  # 初期表示
  def init_app(self) :
    self.titlebar("Help Window", cap.CursesApp.TB_ALIGN_CENTER, cap.CursesApp.REV_GREEN)
    self.statusbar("'q': Quit, 'h': Help", cap.CursesApp.REV_GREEN)
    self.redraw()
    return

  # 再描画
  def redraw(self) :
    self.clear(True)
    self.print("'h' キーでヘルプを表示します。", 20, 10)
    return

  # キー入力ハンドラ
  def handler(self, key) :
    rc = True
    if str(key) == 'h':
      Application.helpWin = not Application.helpWin
      if Application.helpWin :
        self.helpWindow(Application.HELP, "Help")
      else :
        self.redraw()
    elif key == 'q':
      rc = False
    else :
      pass
    return rc

# アプリケーションをインスタンス化して開始
Application()

