#!/usr/bin/python3
#  タイトルバー、ステータスバー、ヘルプウィンドウ、メッセージボックス
from CursesApp import CursesApp
import curses

HELP_TEXT = """
    タイトルバー、ステータスバー、ヘルプウィンドウ、メッセージボックスのテストプログラム
      F1 キーでヘルプを表示する。任意のキー押すとヘルプを閉じる。
      'o' で OKボタンのみを持つメッセージボックスを表示する。
      'y' で YesボタンとNoボタンを持つメッセージボックスを表示する。
      'c' で OKボタンとCancelボタンを持つメッセージボックスを表示する。
      'i' で入力ボックスを表示する。入力文字列はステータスバーに表示される。
      't' でトーストを表示する。
      'q' でテストプログラムを終了する。

       メッセージボックスで Enter キーを押すと、カーソルが点滅しているボタンが選ばれて
       メッセージボックスが閉じる。
       このとき、値 0 (CursesApp.BTN_OK) が返される。
      Tab キーを押すと、ボタンの選択状態が交互に変化する。
      Esc キーを押すと、No ボタンまたは Cancel ボタンが押されたのと同じく
      メッセージボックスが閉じる。
       このとき、値 1 (CursesApp.BTN_CANCEL) が返される。
"""

#
#  アプリケーションクラス
#  =====================
class Application(CursesApp) :

  # コンストラクタ
  def __init__(self) :
    super().__init__()

  # オーバーライド：初期表示
  def init_app(self) :
    self.titlebar("プログラム test_CursesApp2.py", CursesApp.TB_ALIGN_CENTER, 18)
    self.statusbar("初期化完了", 8)
    self.redraw()
    self.hideCursor()

  # クライアント領域描画
  def redraw(self) :
    self.clear(client=True)
    self.print("Screen [width x height] = " + str(self.Columns) + ", " + str(self.Rows), 7, 5)
    self.print("'h' Help Window", 5, 7)
    self.print("'o' OK MessageBox", 5, 8)
    self.print("'y' Yes/No MessageBox", 5, 9)
    self.print("'c' OK/Cancel MessageBox", 5, 10)
    self.print("'i' InputBox", 5, 11)
    self.print("'t' Toast", 5, 12)
    self.print("'q' Quit", 5, 13)

  # キー入力ハンドラ
  def handler(self, key) :
    rc = True
    self.statusbar(key, 8)
    result = ""
    if key == 'q' : # アプリ終了
      rc = False
    elif key == 'h' :
      self.helpWindow(HELP_TEXT, "ヘルプウィンドウ (任意キーを押すとで閉じる)")
    elif key == 'o' :
      result = self.messageBox("   OK ボタンのみのメッセージボックス", CursesApp.MB_OKONLY)
    elif key == 'y' :
      result = self.messageBox("   Yes / No ボタンメッセージボックス", CursesApp.MB_YESNO)
    elif key == 'c' :
      result = self.messageBox("   OK / Cancel ボタンメッセージボックス", CursesApp.MB_OKCANCEL)
    elif key == 'i' :
      result = self.inputBox("値を入力します。")
    elif key == 't' :
      result = self.toast("一時的なメッセージ表示")
    else :
      pass
    self.redraw()
    self.statusbar("key=" + str(key) + " result=" + str(result), 8)
    return rc


# インスタンス化して実行開始
Application()
