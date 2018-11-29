#!/usr/bin/python3
#   フォーム
from CursesApp import CursesApp
import curses
from syslog import syslog

class Application(CursesApp) :
  FORM1_DATA = '''[
 {"type":"label", "name":"label1", "text":"label1: フォームのテスト", "left":5, "top":2, "width":20, "color":3, "attr":0},
 {"type":"button", "name":"ok_button", "text":"  OK  ", "left":10, "top":4, "width":0, "color":9, "attr":0, "click":100},
 {"type":"button", "name":"cancel_button", "text":"  Cancel  ", "left":26, "top":4, "width":0, "color":11, "attr":0, "click":101},
 {"type":"checkbox", "name":"check1", "text":"Check1", "left":20, "top":6, "width":0, "checked":false, "color":1, "attr":0},
 {"type":"radio", "name":"radio1", "text":"Radio1", "group":0, "left":40, "top":6, "width":0, "checked":true, "color":1, "attr":0},
 {"type":"radio", "name":"radio2", "text":"Radio2", "group":0, "left":40, "top":7, "width":0, "checked":false, "color":1, "attr":0},
 {"type":"selector", "name":"selector1","items":["APPLE", "GOOGLE", "AMAZON", "MICROSOFT"], "selected":0, "left":30, "top":9, "width":16, "color":5, "attr":0},
 {"type":"textbox", "name":"textbox1", "text":"", "left":50, "top":10, "width":16, "color":8, "attr":0},
 {"type":"label", "name":"label2","text":"Tab: Select, Enter: OK, Esc: Cancel", "left":10, "top":15, "width":16, "color":6, "attr":0}
]'''

  FORM1 ="form1"
  tagidx = 0

  # コンストラクタ
  def __init__(self) :
    super().__init__()

  # オーバーライド：初期表示
  def init_app(self) :
    self.createForm(Application.FORM1, Application.FORM1_DATA)
    self.titlebar("フォームのテスト", 1, 8)
    self.statusbar("Ready", 8)
    self.redraw()

  # クライアント領域描画
  def redraw(self) :
    self.clear(True)
    self.print("'f'キーを押してください。", 5, 4, 5)
    data = ""  
    data += "check1 = " + (self.formData['check1'] if "check1" in self.formData.keys() else "")
    data += "\n"
    data += "radio1 = " + (self.formData['radio1'] if "radio1" in self.formData.keys() else "")
    data += "\n"
    data += "radio2 = " + (self.formData['radio2'] if "radio2" in self.formData.keys() else "")
    data += "\n"    
    data += "textbox1 = " + (self.formData['textbox1'] if "textbox1" in self.formData.keys() else "")
    data += "\n"
    data += "selector1 = " + (self.formData['selector1'] if "selector1" in self.formData.keys() else "")
    self.printLines(data, 8, 6)
    self.hideCursor()
      
    
  # オーバーライド : キー入力ハンドラ
  def handler(self, key) :
    rv = True  # 戻り値 (OK:True,Cancel:False)
    form_name = self.selectedForm
    if form_name == None :
      if key == 'f' or key == 'F':
        self.selectForm(Application.FORM1)
      else :
        self.forms[Application.FORM1] = None
        rv = False
    elif form_name == Application.FORM1 :
      form1 = self.forms[Application.FORM1]
      if key == '\t' :  # タブ(ウィジェットの移動)
        self.tabidx = self.selectWidget()
        widget = form1[self.tabidx]
        self.setCursorToWidget(widget)  # カーソルをウィジェットへ移動
        if widget['type'] == 'textbox' :
          s = self.enterText(widget)
          self.statusbar(s)
      elif key == '\n' :  # Enter：　OK としてフォームを閉じる
        widget = form1[self.tabidx]
        click = self.buttonPressed(widget)
        if click == 100 :  # OK
          self.redraw()
          self.selectedForm = None
          self.statusbar('OK Clicked')
          self.form_data = True
          self.redraw()
        elif click == 101 : # Cancel
          self.redraw()
          self.selectedForm = None
          self.statusbar('Cancel Clicked')
        else :
          pass
      elif key == '\x1b' : # Esc:　Cancel としてフォームを閉じる。
        self.redraw()
        self.selectedForm = None
        rv = False
      elif key == ' ' :  # チェックボックス、ラジオボタン
        widget = form1[self.tabidx]
        self.changeChecked(widget, form1)
      elif str(key) == 'KEY_UP' :  # セレクタ
        widget = form1[self.tabidx]
        self.selectUp(widget)
      elif str(key) == 'KEY_DOWN' :  # セレクタ
        widget = form1[self.tabidx]
        self.selectDown(widget)
      else :  # その他のキーは無視
        pass
    else :
      self.toast("Fatal Error")
      rv = False
    return rv
        
# インスタンス化して実行開始
Application()

