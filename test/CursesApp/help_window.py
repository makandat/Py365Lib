#!/usr/bin/python3
from Py365Lib import CursesApp as cap

class Application(cap.CursesApp) :
  helpWin = False
  HELP = """Help Window
  Help Window
     HelpWindow
  """

  #
  def init_app(self) :
    self.titlebar("Help Window", 1, 8)
    self.statusbar("Hit F1 key", 8)
    self.redraw()
    return

  #
  def redraw(self) :
    self.clear(True)
    self.print("F1 キーでヘルプを表示します。", 20, 10)
    return

  #
  def handler(self, key) :
    rc = True
    if str(key) == 'KEY_F(1)':
      self.helpWin = not self.helpWin
      if self.helpWin :
        self.helpWindow(Application.HELP, "Help")
      else :
        self.redraw()
    elif key == 'q':
      rc = False
    else :
      pass
    return rc


#
Application()

