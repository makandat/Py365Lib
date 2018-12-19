#!/usr/bin/python3
from Py365Lib import CursesApp as cap

## Application クラス ##
class Application(cap.CursesApp) :
  FORM1 = "form1"
  FORM1_DATA = '''[
{"type":"label", "name":"label1", "text":"Click button", "width":20, "left":30, "top":5,"color":6, "attr":0},
{"type":"button", "name":"button1", "text":" Click ", "width":9, "left":40, "top":7, "color":8, "attr":0, "click":100}    
  ]'''
  count = 0
  tabidx = 1  # ボタンの位置

  # 初期表示
  def init_app(self) :
    self.createForm(Application.FORM1, Application.FORM1_DATA) # フォームを作成
    self.titlebar("Simple Form", 1, Application.REV_WHITE)  # タイトルバーを表示
    self.statusbar("Ready", Application.REV_WHITE)  # ステータスバーを表示
    self.selectForm(Application.FORM1)  # フォームを選択(ウィジェットを表示)
    form1 = self.forms[Application.FORM1]  # 現在のフォーム(form1)
    self.setCursorToWidget(form1[Application.tabidx]) # カーソルをボタンへ移動
    return

  # 再描画
  def redraw(self) :
    self.clear(True)
    return

  # キー入力ハンドラ
  def handler(self, key) :
    form1 = self.forms[Application.FORM1]
    rc = True
    if key == cap.CursesApp.ESC :
      # ESC キーが押されたら、アプリ終了
      rc = False
    elif key == cap.CursesApp.LF :
      # ボタンが押されたら、カウントアップ表示
      widget = form1[Application.tabidx]
      click = self.buttonPressed(widget) # 押されたボタンの値を得る。
      if click == 100 :  # 100 はボタンの click プロパティの値
        Application.count += 1
        self.setLabel("label1", "Clicked {0} times.".format(Application.count))
        if Application.count > 5 :  # ５回押されたらアプリ終了
          rc = False 
    else :
      pass
    return rc


## アプリケーションをインスタンス化して開始
Application()

