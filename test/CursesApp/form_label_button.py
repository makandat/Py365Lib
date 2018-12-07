#!/usr/bin/python3
from Py365Lib import CursesApp as cap


class Application(cap.CursesApp) :
  FORM1 = "form1"
  FORM1_DATA = '''[
{"type":"label", "name":"label1", "text":"Click button", "width":20, "left":30, "top":5,"color":6, "attr":0},
{"type":"button", "name":"button1", "text":" Click ", "width":9, "left":40, "top":7, "color":8, "attr":0, "click":100}    
  ]'''
  tagidx = 0
  count = 0

  #
  def init_app(self) :
    self.createForm(Application.FORM1, Application.FORM1_DATA)
    self.titlebar("Simple Form", 1, 8)
    self.statusbar("Ready", 8)
    self.selectForm(Application.FORM1)
    form1 = self.forms[Application.FORM1]
    self.setCursorToWidget(form1[self.tabidx])
    return

  #
  def redraw(self) :
    self.clear(True)
    return

  #
  def handler(self, key) :
    form1 = self.forms[Application.FORM1]
    rc = True
    if key == cap.CursesApp.ESC :
      # 
      self.redraw()
      self.selectedForm = None
      rc = False
    elif key == cap.CursesApp.LF :
      widget = form1[self.tabidx]
      click = self.buttonPressed(widget)
      if click == 100 :
        self.count += 1
        self.setLabel("label1", "Clicked {0} times.".format(self.count))
        if self.count > 5 :
          rc = False 
    else :
      pass
    return rc


#
Application()

