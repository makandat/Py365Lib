#!/usr/bin/python3

from Py365Lib import CursesApp as cap
from syslog import syslog

## アプリケーションクラス
class Application(cap.CursesApp) :
  # 初期表示
  def init_app(self) :
    formName = self.conf['form']
    self.readFormData(formName, formName + ".json")
    self.titlebar(self.conf['title'], Application.TB_ALIGN_CENTER, 8)
    self.statusbar(self.conf['status'], 8)
    self.selectForm(formName)
    form1 = self.forms[formName]
    cap.CursesApp.tabidx = 0
    widget = form1[cap.CursesApp.tabidx]
    self.setCursorToWidget(widget)
    return

  # 再描画
  def redraw(self) :
    self.clear(True)
    formName = self.selectedForm
    self.selectForm(formName)
    form1 = self.forms[formName]
    self.setCursorToWidget(form1[cap.CursesApp.tabidx])
    return

  # キー入力ハンドラ
  def handler(self, key) :
    formName = self.selectedForm
    form1 = self.forms[formName]
    rc = True
    if key == cap.CursesApp.ESC :
      #  ESC キー
      self.selectedForm = None
      rc = False
    elif key == cap.CursesApp.TAB :
      # TAB キー
      cap.CursesApp.tabidx = self.selectWidget()
      widget = form1[cap.CursesApp.tabidx]
      self.setCursorToWidget(widget)
    elif key == ' ' :
      # 空白キー
      widget = form1[cap.CursesApp.tabidx]
      if widget['type'] == 'radio' or widget['type'] == 'radiobutton':
        self.changeChecked(widget, form1)
      elif widget['type'] == 'checkbox' or widget['type'] == 'check' :
        self.changeChecked(widget, form1)       
        widget["checked"] = not widget["checked"]
      else :
        pass
    elif key == cap.CursesApp.LF :
      #  Enter キー
      widget = form1[cap.CursesApp.tabidx]
      click = self.buttonPressed(widget)
      if click == 100 :
        # OK button
        #  各ウィジェットの値を得る。
        radio = ""
        if self.isChecked("radio1") :
          radio = "Radio1"
        elif self.isChecked("radio2") :
          radio = "Radio2"
        elif self.isChecked("radio3") :
          radio = "Radio3"
        else :
          pass
        self.getProperty(formName, "radio2", "checked")
        self.getProperty(formName, "radio3", "checked")
        status = "Check1 = {0}, Radio = {1}".format(self.getProperty(formName, "check1", "checked"), radio)
        self.setLabel("label1", status)
        # formData を使うと次のように簡単に書ける。
        # self.setLabel("label1", str(self.formData['check1']) + "," + str(self.formData['radio1']) +  "," + str(self.formData['radio2']) + "," + str(self.formData['radio3']))
        self.redraw()
        cap.CursesApp.tabidx = 6  # Cancel ボタン
        widget = form1[cap.CursesApp.tabidx]
        self.setCursorToWidget(widget)
      elif click == 101 :
        # Cancel button
        self.selectedForm = None
        rc = False
      else :
        pass
    else :
      pass
    return rc


#
Application()
