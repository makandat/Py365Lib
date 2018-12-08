#!/usr/bin/python3
from Py365Lib import CursesApp as cap
import curses

class Application(cap.CursesApp) :
  #
  def init_app(self) :
    self.redraw()
    self.hideCursor()
    return

  #
  def redraw(self) :
    self.titlebar("Title bar", Application.TB_ALIGN_CENTER, 14)
    self.statusbar("Status bar", 16)
    x = int((self.Columns - 5) / 2)
    y = int(self.Rows / 2)
    self.print("Hello", x, y, 5)
    return

  #
  def handler(self, key) :
    rc = True
    if key == 'q' :
      rc = False
    return rc


#
Application()

