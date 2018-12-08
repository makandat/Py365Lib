#!/usr/bin/python3

from Py365Lib import CursesApp as cap
from syslog import syslog

class Application(cap.CursesApp) :
  #
  def init_app(self) :
    self.formNames = self.conf['form'].split(",")
    for formName in self.formNames :
      self.readFormData(formName, formName + ".json")
    self.titlebar(self.conf['title'], Application.TB_ALIGN_CENTER, 8)
    self.statusbar(self.conf['status'], 8)
    self.selectForm(self.formNames[0])
    form1 = self.forms[self.formNames[0]]
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
    if key == Application.ESC :
      #  ESC
      self.selectedForm = None
      rc = False
    elif key == Application.TAB :
      self.tabidx = self.selectWidget()
      widget = form1[self.tabidx]
      self.setCursorToWidget(widget)
      if widget['type'] == 'textbox' or widget['type'] == 'text':
        s = self.enterText(widget)
        widget['text'] = s
        #Application.formData[widget['name']] = s
    elif key == ' ' :
      # SPACE
      widget = form1[self.tabidx]
      if widget['type'] == 'check' or widget['type'] == 'checkbox' :
        self.changeChecked(widget, form1)        
        widget['checked'] = not widget['checked']
      else :
        pass
    elif key == Application.LF :
      #  Enter
      widget = form1[self.tabidx]
      click = self.buttonPressed(widget)
      if click == 100 :
        # OK button
        if self.selectedForm == "form1" :
          self.selectForm(self.formNames[1])
          self.redraw()
          # form2 が表示される。
          form2 = self.forms["form2"]
          self.tabidx = 2  # textbox のインデックス
          widget = form2[self.tabidx]
          self.setCursorToWidget(widget)
          if widget['type'] == 'textbox' or widget['type'] == 'text':
            s = self.enterText(widget)
            widget['text'] = s
            widget = form2[self.tabidx]
            self.setCursorToWidget(widget)
        elif self.selectedForm == "form2" :
          self.selectForm(self.formNames[2])
          self.redraw()
          # form3 が表示される。
          self.setLabel("label5", "Check1={0}, Check2={1}, Text1={2}".format(Application.formData['check1'], Application.formData['check2'], Application.formData['text1']))
          self.tabidx = 2
          form3 = self.forms["form3"]
          widget = form3[self.tabidx]
          self.setCursorToWidget(widget)
        elif self.selectedForm == "form3" :
          self.selectForm(self.formNames[1])
          self.redraw()
          # form2 が表示される
          form2 = self.forms["form2"]
          self.tabidx = 2  # textbox のインデックス
          widget = form2[self.tabidx]
          self.setCursorToWidget(widget)
          if widget['type'] == 'textbox' or widget['type'] == 'text':
            s = self.enterText(widget)
            widget['text'] = s
            Application.formData['text1'] = s
            widget = form2[self.tabidx]
            self.setCursorToWidget(widget)
        else :
          raise
      elif click == 101 :
        # Cancel button
        if self.selectedForm == "form1" :
          self.selectedForm = None
          rc = False
        elif  self.selectedForm == "form2" :
          self.selectForm(self.formNames[0])
          self.redraw()
        elif self.selectedForm == "form3" :
           rc = False
        else :
          raise
      else :
        pass
    else :
      pass
    return rc


#
Application()
