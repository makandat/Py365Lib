#!/usr/bin/python3
from Py365Lib import CursesApp as cap, Common

## アプリケーションクラス
class Application(cap.CursesApp) :
  answer = ""  # メッセージボックスが返す値

  # 初期表示
  def init_app(self) :
    self.titlebar("MessageBox", Application.TB_ALIGN_CENTER, Application.REV_WHITE)
    self.statusbar("Ready", Application.REV_WHITE)
    self.__menu()
    return

  # メニューを表示する。
  def __menu(self) :
    self.print("'q': Quit", 10, 4)
    self.print("'O': OK Only MessageBox", 10, 5)
    self.print("'Y': Yes/No MessageBox", 10, 6)
    self.print("'C': OK/Cancel MessageoBox", 10, 7)
    self.print("'T': Toast", 10, 8)
    self.print("'I': InputBox", 10, 9)
    self.print("'A': Alert", 10, 10)
    return

  # 再描画
  def redraw(self) :
    self.clear()
    self.__menu()
    self.hideCursor()
    self.print("answer=" + self.resultText(Application.answer), 20, 2, Application.COL_YELLOW)
    self.titlebar("MessageBox", Application.TB_ALIGN_CENTER, Application.REV_WHITE)
    self.statusbar("Ready", Application.REV_WHITE)
    return

  # 結果表示
  def resultText(self, ans) :
    result = "No Answer"
    if Common.isset(ans) :
      if ans == Application.BTN_OK :
        result = "CursesApp.BTN_OK"
      elif ans == Application.BTN_CANCEL :
        result = "CursesApp.BTN_CANCEL"
      else :
        result = ans
    else :
      pass
    return result

  # キー入力ハンドラ
  def handler(self, key) :
    rc = True
    if key == 'q' :
      rc = False
    elif key == 'O' :
      #  OK only メッセージボックス
      self.messageBox("OK Only Message Box", Application.MB_OKONLY)
      Application.answer = ""
    elif key == 'Y' :
      # Yes/No メッセージボックス
      Application.answer = ans = self.messageBox("Yes/No Message Box", Application.MB_YESNO)
    elif key == 'C' :
      # OK/Cancel メッセージボックス
      Application.answer = self.messageBox("OK/Cancel Message Box", Application.MB_OKCANCEL)
    elif key == 'T' :
      # トースト
      self.toast("Shall close soon.")
      Application.answer = ""
    elif key == 'I' :
      # 入力ボックス
      Application.answer = self.inputBox("Enter your name.")
    elif key == 'A' :
      # alert
      self.alert()
    else :
      pass
    self.redraw()
    return rc

## アプリケーションをインスタンス化して開始。
Application()

