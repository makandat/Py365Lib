#!/usr/bin/python3
from Py365Lib import CursesApp as cap
from syslog import syslog

class Application(cap.CursesApp) :
  # 初期化
  def init_app(self) :
    formName = self.conf['form']
    # ウィジェットデータを JSON ファイルからロードする。
    self.readFormData(formName, formName + ".json")
    self.titlebar(self.conf['title'], cap.CursesApp.TB_ALIGN_CENTER, 8)
    self.statusbar(self.conf['status'], 8)
    self.selectForm(formName)
    form1 = cap.CursesApp.forms[formName]
    self.setCursorToWidget(form1[cap.CursesApp.tabidx])
    cap.CursesApp.tabidx = 1
    widget = form1[cap.CursesApp.tabidx]
    # 最初のウィジェットがテキストボックスなのでキー入力モードにする。
    s = self.enterText(widget)
    cap.CursesApp.tabidx = 2
    self.setCursorToWidget(form1[cap.CursesApp.tabidx])  # フォーカスをボタンへ
    return

  # 再描画
  def redraw(self) :
    self.clear(True)
    formName = self.selectedForm
    self.selectForm(formName)
    form1 = cap.CursesApp.forms[formName]
    cap.CursesApp.tabidx = 1
    self.setCursorToWidget(form1[cap.CursesApp.tabidx])
    return

  # ハンドラ
  def handler(self, key) :
    formName = self.selectedForm
    form1 = cap.CursesApp.forms[formName]
    rc = True
    if key == cap.CursesApp.ESC :
      # ESC キーなら終了
      self.selectedForm = None
      rc = False
    elif key == cap.CursesApp.TAB :
      # TAB キー
      cap.CursesApp.tabidx = self.selectWidget()  # 次のウィジェットのタブインデックスを得る。
      widget = form1[cap.CursesApp.tabidx]
      self.setCursorToWidget(widget)  # カーソルをウィジェットへ移動
      if widget['type'] == 'text' :
        # テキストボックスなら文字列入力
        self.enterText(widget)
        self.setCursorToWidget(form1[cap.CursesApp.tabidx])
    elif key == cap.CursesApp.LF :
      # Enter キーかつボタンなら押されたボタンの種別を得る。
      widget = form1[cap.CursesApp.tabidx]
      click = self.buttonPressed(widget)
      if click == 100 :
        # OK ボタンの時
        s = self.getLabel("text1")
        self.messageBox("OK button clicked.  price = " + s)
        self.statusbar(s, cap.CursesApp.REV_WHITE)
        self.redraw()
        cap.CursesApp.tabidx = 3 # Cancel ボタン
        self.setCursorToWidget(form1[cap.CursesApp.tabidx])  
      elif click == 101 :
        # Cancel ボタンの時
        self.selectedForm = None
        rc = False
      else :
        # ボタンでない場合
        pass
    else :
      pass
    return rc

# アプリケーション
Application()

