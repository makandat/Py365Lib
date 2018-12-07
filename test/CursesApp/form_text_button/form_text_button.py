#!/usr/bin/python3
from Py365Lib import CursesApp as cap
from syslog import syslog

class Application(cap.CursesApp) :
  #
  def init_app(self) :
    formName = self.conf['form']
    self.readFormData(formName, formName + ".json")
    self.titlebar(self.conf['title'], 1, 8)
    self.statusbar(self.conf['status'], 8)
    self.selectForm(formName)
    form1 = self.forms[formName]
    self.setCursorToWidget(form1[self.tabidx])
    self.tabidx = 0
    widget = form1[self.tabidx]
    s = self.enterText(widget)
    self.statusbar(s)       
    return

  #
  def redraw(self) :
    self.clear(True)
    formName = self.selectedForm
    self.selectForm(formName)
    form1 = self.forms[formName]
    self.setCursorToWidget(form1[self.tabidx])
    return

  #
  def handler(self, key) :
    formName = self.selectedForm
    form1 = self.forms[formName]
    rc = True
    if key == cap.CursesApp.ESC :
      # 
      self.selectedForm = None
      rc = False
    elif key == cap.CursesApp.TAB :
      self.tabidx = self.selectWidget()
      widget = form1[self.tabidx]
      self.setCursorToWidget(widget)  # カーソルをウィジェットへ移動
      if widget['type'] == 'text' :
        s = self.enterText(widget)
        self.statusbar(s)       
    elif key == cap.CursesApp.LF :
      widget = form1[self.tabidx]
      click = self.buttonPressed(widget)
      if click == 100 :
        self.messageBox("OK button clicked")
        self.redraw()
      elif click == 101 :
        self.selectedForm = None
        rc = False
      else :
        pass
    else :
      pass
    return rc


#
Application()

