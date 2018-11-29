#
#  TkApp クラス
#    version 0.13  2018-11-14
import json, os
import tkinter as tk
#from syslog import syslog

#
#  Tkinter Application クラス
# ===============================
class TkApp(tk.Frame) :
  widgets = []  # ウィジェットのリスト
  didgets = {}  # ウィジェットのリストへのポインタのリスト (キーはウィジェットの名前)
  layouts = []  # ウィジェットのレイアウトのリスト
  commands = {} # ウィジェットのコマンドのハッシュ (キーはウィジェットの名前)
  # JSON ファイル、オプションのキー分類
  Keys_TkApp = ("name", "type", "layout", "container")
  Keys_place = ( "x", "y", "relx", "rely" )
  Keys_grid = ( "row", "column", "rowspan", "columnspan", "sticky", "padx", "pady", "ipadx", "ipady" )
  Keys_pack = ( "anchor", "expand", "fill", "ipadx", "ipady", "padx", "pady", "side" )

  # コンストラクタ
  def __init__(self, master, winprop, filename="") :
    super().__init__(master)
    self.__master = master
    fixedborder = False
    if "fixedborder" in winprop :
      fixedborder = winprop['fixedborder']
    self.setMasterProperties(winprop['title'], winprop['left'], winprop['top'], winprop['width'], 
      winprop['height'], fixedborder)
    self.pack()
    self.createWidgets(filename)
    return

  # マスターウィンドウの属性を設定する。
  def setMasterProperties(self, title, x, y, width, height, fixedborder=False) :
    self.__master.geometry(f"{width}x{height}+{x}+{y}")
    self.__master.title(title)
    if fixedborder :
      self.__master.resizable(0, 0)
    return
    
  # ウィジェットを構築する。
  def createWidgets(self, filename) :
    self.widgets = list()
    self.didgets = dict()
    self.layouts = list()
    self.commands = dict()

    if os.path.isfile(filename) :
      # json ファイルがある場合
      self.loadWidgets(filename)
      n = len(self.widgets)
      for i in range(n) :
        c = self.widgets[i]
        lay = self.layouts[i]
        if lay['type'] == "place" :
          if 'x' in lay.keys() :
            c.place(x=lay['x'], y=lay['y'])
          elif 'relx' in lay.keys() :
            c.place(relx=lay['relx'], rely=lay['rely'])
          else :
            c.pack()
        elif lay['type'] == "grid" :
          if 'column' in lay :
            c.grid(column=lay['column'], row=lay['row'])
          else :
            c.pack()
        elif lay['type'] == "pack" :
          if 'side' in lay :
            c.pack(side=lay['side'])
          else :
            c.pack()
        else :
          pass
    else :
      # json ファイルがない場合
      self.label1 = tk.Label(text="json ファイルがない場合は、createWidgets メソッドをオーバーライドします。", pady=8, fg="green")
      self.label1.pack()
      self.button1 = tk.Button(text="Close", command=self.__master.destroy)
      self.button1.pack()
    return
    
  # JSON ファイルからウィジェットを構築する。
  def loadWidgets(self, filename) :
    items = []
    parent = self.__master
    with open(filename) as f :
      s = f.read()
      items = json.loads(s)
      # ウィジェットを作成
      self.createWidgetItems(items, parent)
      # コマンド (command) の設定
      # self.setCommands()
    return

  # ウィジェットを作成
  def createWidgetItems(self, items, parent) :
    it = iter(items)
    while True :
      try :
        item = next(it)
      except :
        break
      if item["type"] == "button" :
        c = tk.Button(parent)
        self.__appendKeys(c, item)
      elif item["type"] == "label" :
        c = tk.Label(parent)
        self.__appendKeys(c, item)
      elif item["type"] == "entry" or item["type"] == "text" or item["type"] == "textbox" :
        c = tk.Entry(parent)
        self.__appendKeys(c, item)
      elif item["type"] == "check" or item["type"] == "checkbox":
        c = tk.Checkbutton(parent, text=item["text"])
        self.__appendKeys(c, item)
      elif item["type"] == "radio" or item["type"] == "radiobutton":
        c = tk.Radiobutton(parent, text=item["text"])
        self.__appendKeys(c, item)
      elif item["type"] == "list" or item["type"] == "listbox":
        c = tk.Listbox(parent)
        self.__appendKeys(c, item)
      elif item["type"] == "frame" :
        f = tk.Frame(parent)
        for k in item :
          if TkApp.isWidgetKey(k) :
            f[k] = item[k]
        n = len(self.widgets) - 1
        if "layout" in item.keys() :
          self.layouts.append({"type":item["layout"], "widget":item["type"], "border":item["border"], "relief":item["relief"]})
        else :
          self.layouts.append({"type":"pack", "widget":item["type"], "border":item["border"], "relief":item["relief"]})
        self.widgets.append(f)
        self.didgets[item['name']] = n
        self.createWidgetItems(item["container"], f)
      else :
        pass
    return

  #  widgets, layout にウィジェット(c)の情報を追加する。
  def __appendKeys(self, c, item) :
    for k in item :
      if TkApp.isWidgetKey(k) :
        c[k] = item[k]
    self.widgets.append(c)
    n = len(self.widgets) - 1
    self.didgets[item['name']] = n
    layout = "pack"
    if "layout" in item.keys() :
      layout = item["layout"]
    self.layouts.append({"type":layout, "name":item["name"], "widget":item["type"]})
    ll = self.layouts[n]
    for k in item :
      if TkApp.isLayoutKey(k, layout) :
        ll[k] = item[k] 
    return

  # command オプションの修正
  def setCommands(self) :
    for i in range(len(self.widgets)) :
      wi = self.widgets[i]
      if "command" in wi.keys() :
        name = self.getWidgetName(i)
        self.setWidget(name, "command", self.commands[name])
    return

  # キーがウィジェットのものか判別する。
  @classmethod
  def isWidgetKey(cls, key) :
    b = True
    if key in cls.Keys_TkApp :
      b = False
    elif key in cls.Keys_pack :
      b = False
    elif key in cls.Keys_grid :
      b = False
    elif key in cls.Keys_place :
      b = False
    else :
      pass
    return b
    
  # キーが TkApp 独自のものか確認する。
  @classmethod
  def isTkAppKey(cls, key) :
    return (key in cls.Keys_TkApp)

  # キーがレイアウトのものか確認する。
  @classmethod
  def isLayoutKey(cls, key, layout="pack") :
    b = False
    if layout == "place" :
      b = key in cls.Keys_place
    elif layout == "grid" :
      b = key in cls.Keys_grid
    else :
      b = key in cls.Keys_pack
    return b

  # ウィンドウサイズを得る。
  def getWindowSize(self, win) :
    width = win.winfo_width()
    height = win.winfo_height()
    return (width, height)

  # スクリーンサイズを得る。
  def getScreenSize(self) :
    width = self.__master.winfo_screenwidth()
    height = self.__master.winfo_screenheight()
    return (width, height)

  # ウィジェットオブジェクトを名前から得る。
  def getWidget(self, name) :
    i = self.didgets[name]
    w = self.widgets[i]
    return w

  # 名前で指定したウィジェットのオプションを変更（あるいは追加）する。
  def setWidget(self, name, key, value) :
    i = self.didgets[name]
    w = self.widgets[i]
    w[key] = value
    return

  # 指定した番号のウィジェットの名前を得る。
  def getWidgetName(self, idx) :
    name = ""
    for k, v in self.didgets.items() :
      if v == idx :
        name = k
        break
    return name



'''  以下はインスタンス化の仕方
root = tk.Tk()
app = TkApp(master=root, filename="TkApp.json")
app.mainloop()
'''
