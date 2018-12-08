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
    self.tabidx = 1
    widget = form1[self.tabidx]
    self.setCursorToWidget(widget)
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
      #  ESC
      self.selectedForm = None
      rc = False
    elif key == cap.CursesApp.TAB :
      self.tabidx = self.selectWidget()
      widget = form1[self.tabidx]
      self.setCursorToWidget(widget)
    elif str(key) == 'KEY_UP' :
      widget = form1[self.tabidx]
      self.selectUp(widget)
    elif str(key) == 'KEY_DOWN' :
      widget = form1[self.tabidx]
      self.selectDown(widget)
    elif key == cap.CursesApp.LF :
      #  Enter
      widget = form1[self.tabidx]
      click = self.buttonPressed(widget)
      if click == 100 :
        # OK button
        # formData を使うと次のように簡単に書ける。
        self.setLabel("label2", "Select index = {0}".format(Application.formData['selector1']))
        self.redraw()
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
