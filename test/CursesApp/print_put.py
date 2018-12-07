#!/usr/bin/python3
from Py365Lib import CursesApp as cap
import curses


class Application(cap.CursesApp) :
  thekey = '-'

  #
  def init_app(self) :
    self.print("'0': putchar(), '1': putch(), '2': print(), '3': printLines(), 'q': Quit", 10, 8)
    self.hideCursor()
    self.redraw()
    return

  #
  def redraw(self) :
    if self.thekey =='0' :
      self.clear()
      self.setCursorPosition(20, 1)
      i = 0
      for a in range(ord('0'), ord(':')) :
        self.putchar(chr(a), 20, i + 1)
        i += 1
    elif self.thekey == '1' :
      self.putch('X')
    elif self.thekey == '2' :
      self.clear()
      self.print("self.print()", 10, 5, 6, curses.A_BOLD)
    elif self.thekey == '3' :
      self.clear()
      self.printLines('''printLines
    printLines
            printLines
''',
      10, 5, 5)
    else :
      pass
    return

  #
  def handler(self, key) :
    rc = True
    if key == 'q' :
      rc = False
    elif key == '0' or key == '1' or key == '2' or key == '3' :
      self.thekey = key
      self.redraw()
    else :
      pass
    return rc


#
Application()

