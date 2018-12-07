#!/usr/bin/python3
from Py365Lib import CursesApp as cap

class Application(cap.CursesApp) :
  answer = ""

  #
  def init_app(self) :
    self.__menu()
    return

  def __menu(self) :
    self.print("'q': Quit", 10, 4)
    self.print("'O': OK Only MessageBox", 10, 5)
    self.print("'Y': Yes/No MessageBox", 10, 6)
    self.print("'C': OK/Cancel MessageoBox", 10, 7)
    self.print("'T': Toast", 10, 8)
    self.print("'I': InputBox", 10, 9)
    return

  #
  def redraw(self) :
    self.clear()
    self.__menu()
    self.print("answer=" + str(self.answer), 20, 2, 5)
    return

  #
  def handler(self, key) :
    rc = True
    if key == 'q' :
      rc = False
    elif key == 'O' :
      #
      self.messageBox("OK Only Message Box", 0)
      self.answer = ""
    elif key == 'Y' :
      #
      self.answer = ans = self.messageBox("Yes/No Message Box", 1)
    elif key == 'C' :
      #
      self.answer = self.messageBox("OK/Cancel Message Box", 2)
    elif key == 'T' :
      #
      self.toast("Shall close soon.")
      self.answer = ""
    elif key == 'I' :
      #
      self.answer = self.inputBox("Enter your birth year.")
    else :
      pass
    self.redraw()
    return rc

#
Application()

