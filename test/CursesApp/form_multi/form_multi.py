#!/usr/bin/python3
#  複数フォーム
from Py365Lib import CursesApp as cap

# アプリケーションクラス
class Application(cap.CursesApp) :
  # 初期表示
  def init_app(self) :
    # 構成ファイル (AppConf.ini) から読み取ったデータからフォーム名を得る。
    self.formNames = self.conf['form'].split(",")
    for formName in self.formNames :
      # フォーム名から JSON ファイル名を決めて、ウィジェット定義データを取得する。
      self.readFormData(formName, formName + ".json")
    # タイトルバーとステータスバーを表示
    self.titlebar(self.conf['title'], Application.TB_ALIGN_CENTER, Application.REV_WHITE)
    self.statusbar(self.conf['status'], Application.REV_WHITE)
    # 先頭のフォームを表示する。
    self.selectForm(self.formNames[0])
    form1 = self.forms[self.formNames[0]]
    # カーソルを最初のラベル以外のウィジェットへ移動
    cap.CursesApp.tabidx = 1
    widget = form1[cap.CursesApp.tabidx]
    self.setCursorToWidget(widget)
    return

  # 再描画
  def redraw(self) :
    # 画面(クライアント領域のみ)をクリア
    self.clear(True)
    # 現在のフォーム名からフォームを選択(表示する)
    formName = self.selectedForm
    self.selectForm(formName)
    # カーソルを最初のラベル以外のウィジェットへ移動
    form1 = self.forms[formName]
    self.setCursorToWidget(form1[cap.CursesApp.tabidx])
    return

  # キー入力ハンドラ
  def handler(self, key) :
    # form1 に現在のフォームオブジェクトを代入
    formName = self.selectedForm
    form1 = self.forms[formName]
    rc = True
    if key == Application.ESC :
      #  ESC キー
      # アプリケーション終了
      self.selectedForm = None
      rc = False
    elif key == Application.TAB :
      # TAB キー
      #  次のウィジェットへフォーカス移動
      cap.CursesApp.tabidx = self.selectWidget()
      widget = form1[cap.CursesApp.tabidx]
      self.setCursorToWidget(widget)
      if widget['type'] == 'textbox' or widget['type'] == 'text':
        # そのウィジェットがテキストボックスならキーボード入力
        s = self.enterText(widget)
        widget['text'] = s
    elif key == ' ' :
      # SPACE キー
      widget = form1[cap.CursesApp.tabidx]
      if widget['type'] == 'check' or widget['type'] == 'checkbox' :
        # フォーカスされているウィジェットがチェックボックスなら、チェック状態を反転
        self.changeChecked(widget, form1)        
        widget['checked'] = not widget['checked']
      else :
        pass
    elif key == Application.LF :
      #  Enter キー
      #  ボタンのクリック値を得る。
      widget = form1[cap.CursesApp.tabidx]
      click = self.buttonPressed(widget)
      if click == 100 :
        # OK ボタン
        if self.selectedForm == "form1" :
          # 現在のフォームが form1
          self.selectForm(self.formNames[1])
          self.redraw()
          # form2 が表示される。
          form2 = self.forms["form2"]
          cap.CursesApp.tabidx = 2  # textbox のインデックス
          widget = form2[cap.CursesApp.tabidx]
          self.setCursorToWidget(widget)
          if widget['type'] == 'textbox' or widget['type'] == 'text':
            s = self.enterText(widget)
            widget['text'] = s
            widget = form2[cap.CursesApp.tabidx]
            self.setCursorToWidget(widget)
        elif self.selectedForm == "form2" :
          # 現在のフォームが form2
          self.selectForm(self.formNames[2])
          self.redraw()
          # form3 が表示される。
          self.setLabel("label5", "Check1={0}, Check2={1}, Text1={2}".format(Application.formData['check1'], Application.formData['check2'], Application.formData['text1']))
          cap.CursesApp.tabidx = 2
          form3 = self.forms["form3"]
          widget = form3[cap.CursesApp.tabidx]
          self.setCursorToWidget(widget)
        elif self.selectedForm == "form3" :
          # 現在のフォームが form3
          self.selectForm(self.formNames[1])
          self.redraw()
          # form2 が表示される
          form2 = self.forms["form2"]
          cap.CursesApp.tabidx = 2  # textbox のインデックス
          widget = form2[cap.CursesApp.tabidx]
          self.setCursorToWidget(widget)
          if widget['type'] == 'textbox' or widget['type'] == 'text':
            s = self.enterText(widget)
            widget['text'] = s
            Application.formData['text1'] = s
            widget = form2[cap.CursesApp.tabidx]
            self.setCursorToWidget(widget)
        else :
          raise
      elif click == 101 :
        # Cancel ボタンの時
        if self.selectedForm == "form1" :
          # form1 ならアプリケーション終了
          self.selectedForm = None
          rc = False
        elif  self.selectedForm == "form2" :
          # form2 なら form1 へもどる。
          self.selectForm(self.formNames[0])
          self.redraw()
        elif self.selectedForm == "form3" :
          # form3 ならアプリケーション終了
           rc = False
        else :
          raise
      else :
        pass
    else :
      pass
    return rc


# アプリケーションをインタンス化して開始
Application()
