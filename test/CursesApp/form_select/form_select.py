#!/usr/bin/python3

from Py365Lib import CursesApp as cap
from syslog import syslog

## アプリケーションクラス
class Application(cap.CursesApp) :
  # 初期表示
  def init_app(self) :
    formName = self.conf['form']
    self.readFormData(formName, formName + ".json")
    self.titlebar(self.conf['title'], 1, cap.CursesApp.REV_WHITE)
    self.statusbar(self.conf['status'], cap.CursesApp.REV_WHITE)
    self.selectForm(formName)
    form1 = cap.CursesApp.forms[formName]
    cap.CursesApp.tabidx = 1
    widget = form1[cap.CursesApp.tabidx]
    self.setCursorToWidget(widget)
    return

  # 再描画
  def redraw(self) :
    self.clear(True)
    formName = self.selectedForm
    self.selectForm(formName)
    form1 = cap.CursesApp.forms[formName]
    self.setCursorToWidget(form1[cap.CursesApp.tabidx])
    return

  # キー入力ハンドラ
  def handler(self, key) :
    formName = self.selectedForm
    form1 = cap.CursesApp.forms[formName]
    rc = True
    if key == cap.CursesApp.ESC :
      #  ESC キー
      self.selectedForm = None
      rc = False  # アプリ終了
    elif key == cap.CursesApp.TAB :
      # TAB キー
      cap.CursesApp.tabidx = self.selectWidget()
      widget = form1[cap.CursesApp.tabidx]
      #if widget['type'] == 'selector' :
      #  self.selectSelectorItem(widget, 0)
      self.setCursorToWidget(widget)
    elif str(key) == 'KEY_UP' :
      # 上向き矢印キー
      widget = form1[cap.CursesApp.tabidx]
      self.selectUp(widget)
    elif str(key) == 'KEY_DOWN' :
      # 下向き矢印キー
      widget = form1[cap.CursesApp.tabidx]
      self.selectDown(widget)
    elif key == cap.CursesApp.LF :
      #  Enter キー
      widget = form1[cap.CursesApp.tabidx]
      click = self.buttonPressed(widget)
      if click == 100 :
        # OK button
        # formData を使うと次のように簡単に書ける。
        self.setLabel("label2", "Select index = {0}".format(Application.formData['selector1']))
        self.redraw()
        cap.CursesApp.tabidx = self.selectWidget()
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
