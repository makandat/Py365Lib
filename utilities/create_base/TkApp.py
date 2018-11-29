#
#  TkApp クラス
#    version 1.00  2018-11-25
#
import json, os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, filedialog
from syslog import syslog

#
#  Tkinter Application クラス
# ===============================
class TkApp(tk.Frame) :
  widgets = []  # ウィジェットのリスト
  didgets = {}  # ウィジェットのリストへのポインタのリスト (キーはウィジェットの名前)
  layouts = []  # ウィジェットのレイアウトのリスト
  commands = {} # ウィジェットのコマンドのハッシュ (キーはウィジェットの名前)
  images = []   # 画像のリスト
  menubar = None    # メニューバー
  menudata = None   # メニューデータ
  radioval = None  # ラジオボックスの値
  textvals = {}   # テキストボックスの値 (キーは名前)
    
  # JSON ファイル、オプションのキー分類
  Keys_TkApp = ("name", "type", "layout", "container")
  Keys_place = ( "x", "y", "relx", "rely" )
  Keys_grid = ( "row", "column", "rowspan", "columnspan", "sticky", "padx", "pady", "ipadx", "ipady" )
  Keys_pack = ( "anchor", "expand", "fill", "ipadx", "ipady", "padx", "pady", "side" )
  Keys_menu = ( "menulist", "submenulist" )

  # コンストラクタ
  def __init__(self, master, winprop, filename="") :
    super().__init__(master)
    self.__master = master
    self.fixedborder = False
    self.radioval = tk.IntVar()  # ラジオボックスの値
    self.radioval.set(0)
    if "fixedborder" in winprop :
      self.fixedborder = winprop['fixedborder']
    self.setMasterProperties(winprop['title'], winprop['left'], winprop['top'], winprop['width'], 
      winprop['height'], self.fixedborder)
    self.pack()
    self.createWidgets(filename)
    return

  # マスターウィンドウの属性を設定する。
  def setMasterProperties(self, title, x, y, width, height, fixedborder=False) :
    self.__master.geometry(f"{width}x{height}+{x}+{y}")
    self.__master.title(title)
    if self.fixedborder :
      self.__master.resizable(0, 0)
    return
    
  # ウィジェットを構築する。
  def createWidgets(self, filename) :
    self.widgets = list()
    self.didgets = dict()
    self.layouts = list()
    self.commands = dict()
    self.images = list()

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
           self.__gridder(lay, c)
        elif lay['type'] == "pack" :
           self.__packer(lay, c)
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
    return

  # ウィジェットを作成
  def createWidgetItems(self, items, parent) :
    it = iter(items)
    while True :
      try :
        item = next(it)
      except :
        break
      if item["type"] == "button" :  # ボタン
        c = tk.Button(parent)
        self.__appendKeys(c, item)
      elif item["type"] == "label" :  # ラベル
        c = tk.Label(parent)
        self.__appendKeys(c, item)
      elif item["type"] == "entry" or item["type"] == "text" or item["type"] == "textbox" : # テキストボックス
        self.textvals[item['name']] = tk.StringVar()
        if "width" in item and "text" in item:
          self.textvals[item['name']].set(item["text"])
          c = tk.Entry(parent, width=item["width"], textvariable=self.textvals[item['name']])
          c.delete(0, tk.END)
          c.insert(0, item["text"])
        elif "width" in item and "text" in item == False :
          c = tk.Entry(parent, width=item["width"], textvariable=self.textvals[item['name']])
        elif "width" in item == False and "text" in item == True :
          c = tk.Entry(parent, width=item["width"], textvariable=self.textvals[item['name']])
          c.delete(0, tk.END)
          c.insert(0, item["text"])
        else :
          c = tk.Entry(parent, textvariable=self.textvals[item['name']])
        self.__appendKeys(c, item)
      elif item["type"] == "check" or item["type"] == "checkbox": # チェックボックス
        c = ttk.Checkbutton(parent, text=item["text"])
        self.__appendKeys(c, item)
      elif item["type"] == "radio" or item["type"] == "radiobutton":  # ラジオボタン
        c = ttk.Radiobutton(parent, text=item["text"], variable=self.radioval, value=item['value'])
        self.__appendKeys(c, item)
      elif item["type"] == "list" or item["type"] == "listbox":  # リストボックス
        c = tk.Listbox(parent)
        self.__appendKeys(c, item)
      elif item["type"] == "frame" : # フレーム
        if "text" in item.keys() :
          f = ttk.Labelframe(parent, text=item["text"])
        else :
          f = tk.Frame(parent)
        for k in item :
          if TkApp.isWidgetKey(k) :
            f[k] = item[k]
        n = len(self.widgets) - 1
        if "relief" in item :
          item["relief"] = "groove"
        if "border" in item :
          item["border"] = 3
        if "layout" in item.keys() :
          if item["layout"] == "grid" and "column" in item :
            self.layouts.append({"type":item["layout"], "widget":item["type"], "column":item["column"], "row":item["row"], "border":item["border"], "relief":item["relief"]})
          elif item["layout"] == "grid" and "column" in item and "padx" in item:
            self.layouts.append({"type":item["layout"], "widget":item["type"], "column":item["column"], "row":item["row"], "border":item["border"], "relief":item["relief"], "padx":item["padx"], "pady":item["pady"]})
          elif item["layout"] == "place" and ("x" in item or "relx" in item) :
            self.layouts.append({"type":item["layout"], "widget":item["type"], "x":item["x"], "y":item["y"], "border":item["border"], "relief":item["relief"]})
          else :  # pack
            self.layouts.append({"type":item["layout"], "widget":item["type"], "border":item["border"], "relief":item["relief"]})
        else :
          self.layouts.append({"type":"pack", "widget":item["type"], "border":item["border"], "relief":item["relief"]})
        self.widgets.append(f)
        self.didgets[item['name']] = n
        self.createWidgetItems(item["container"], f)
      elif item["type"] == "menubar" :  # メニュー
        mb = tk.Menu(parent)  # parent = root であること
        self.menubar = mb
        parent.config(menu=mb)
        self.menudata = item
      elif item["type"] == "image" or item["type"] == "picture" : # 画像
        img = tk.PhotoImage(file=item["file"])
        self.images.append(img)
        c = tk.Label(parent, image=img)
        item.pop('file')  # キー 'file' を削除
        item['type'] = 'label'
        self.__appendKeys(c, item)
      else :
        pass
    return

  #  widgets, layout にウィジェット(c)の情報を追加する。
  def __appendKeys(self, c, item) :
    # item のキーに対応するウィジェットのウィジェットキーの値を設定
    for k in item :
      if TkApp.isWidgetKey(k) :
        if k == 'items' and (item['type'] == 'list' or item['type'] == 'listbox') :
          for it in item[k] :
            c.insert("end", it)
        else :
          c[k] = item[k]
    # ウィジェットのコレクションに c を追加
    self.widgets.append(c)
    n = len(self.widgets) - 1
    self.didgets[item['name']] = n
    layout = "pack"
    if "layout" in item.keys() :
      layout = item["layout"]
    self.layouts.append({"type":layout, "name":item["name"], "widget":item["type"]})
    # レイアウトのコレクションに item のレイアウトキーの値を設定
    ll = self.layouts[n]
    for k in item :
      if TkApp.isLayoutKey(k, layout) :
        ll[k] = item[k] 
    return

  # メニュー項目を追加する。
  def __appendMenuItem(self, menu, menulist) :
    i = 0
    for item in menulist :
      if item['type'] == 'menuitem' :
        menu.add_command(label=item['text'], command=self.commands[item['command']])
        i += 1
      elif item['type'] == 'separator' :
        menu.add_separator()
      else :
        pass
    return

  # command オプションの修正
  def setCommands(self) :
    # メニュー以外のウィジェット
    for i in range(len(self.widgets)) :
      wi = self.widgets[i]
      if "command" in wi.keys() :
        name = self.getWidgetName(i)
        if name in self.commands :
          self.setWidget(name, "command", self.commands[name])
        else :
          pass
      else :
        pass
    # メニュー
    if self.menudata == None :
      return
    for ml in self.menudata['menulist'] :
      if ml['type'] == 'topmenu' and 'submenulist' in ml :
        menu1 = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label=ml['text'], menu=menu1)
        self.__appendMenuItem(menu1, ml['submenulist'])
      else :
        pass
    return

  # pack レイアウト
  def __packer(self, layout, widget) :
    if (('anchor' in layout) == True) and (('side' in layout) == True) and (('fill' in layout) == True) and (('expand' in layout) == True) and (('padx' in layout) == True) and (('pady' in layout) == True) and (('ipadx' in layout) == True) and (('ipady' in layout) == True) :
      widget.pack(anchor=layout['anchor'], side=layout['side'], fill=layout['fill'], expand=layout['expand'], padx=layout['padx'], pady=layout['pady'], ipadx=layout['ipadx'], ipady=layout['ipady'])
    elif (('anchor' in layout) == True) and (('side' in layout) == False) and (('fill' in layout) == False) and (('expand' in layout) == False) and (('padx' in layout) == False) and (('pady' in layout) == False) and (('ipadx' in layout) == False) and (('ipady' in layout) == False) :
      widget.pack(anchor=layout['anchor'])
    elif (('anchor' in layout) == False) and (('side' in layout) == True) and (('fill' in layout) == False) and (('expand' in layout) == False) and (('padx' in layout) == False) and (('pady' in layout) == False) and (('ipadx' in layout) == False) and (('ipady' in layout) == False) :
      widget.pack(side=layout['side'])
    elif (('anchor' in layout) == False) and (('side' in layout) == False) and (('fill' in layout) == True) and (('expand' in layout) == False) and (('padx' in layout) == False) and (('pady' in layout) == False) and (('ipadx' in layout) == False) and (('ipady' in layout) == False):
      widget.pack(fill=layout['fill'])
    elif (('anchor' in layout) == False) and (('side' in layout) == False) and (('fill' in layout) == False) and (('expand' in layout) == True) and (('padx' in layout) == False) and (('pady' in layout) == False) and (('ipadx' in layout) == False) and (('ipady' in layout) == False):
      widget.pack(expand=layout['expand'])
    elif (('anchor' in layout) == True) and (('side' in layout) == False) and (('fill' in layout) == True) and (('expand' in layout) == False) and (('padx' in layout) == False) and (('pady' in layout) == False) and (('ipadx' in layout) == False) and (('ipady' in layout) == False):
      widget.pack(anchor=layout['anchor'], fill=layout['fill'])
    elif (('anchor' in layout) == True) and (('side' in layout) == True) and (('fill' in layout) == False) and (('expand' in layout) == False) and (('padx' in layout) == False) and (('pady' in layout) == False) and (('ipadx' in layout) == False) and (('ipady' in layout) == False):
      widget.pack(anchor=layout['anchor'], side=layout['side'])
    elif (('anchor' in layout) == True) and (('side' in layout) == True) and (('fill' in layout) == True) and (('expand' in layout) == False) and (('padx' in layout) == False) and (('pady' in layout) == False) and (('ipadx' in layout) == False) and (('ipady' in layout) == False):
      widget.pack(anchor=layout['anchor'], side=layout['side'], fill=layout['fill'])
    elif (('anchor' in layout) == False) and (('side' in layout) == False) and (('fill' in layout) == False) and (('expand' in layout) == False) and (('padx' in layout) == False) and (('pady' in layout) == True) and (('ipadx' in layout) == False) and (('ipady' in layout) == False):
      widget.pack(pady=layout['pady'])
    elif (('anchor' in layout) == False) and (('side' in layout) == False) and (('fill' in layout) == False) and (('expand' in layout) == False) and (('padx' in layout) == True) and (('pady' in layout) == True) and (('ipadx' in layout) == False) and (('ipady' in layout) == False):
      widget.pack(padx=layout['padx'], pady=layout['pady'])
    elif (('anchor' in layout) == True) and (('side' in layout) == False) and (('fill' in layout) == False) and (('expand' in layout) == False) and (('padx' in layout) == True) and (('pady' in layout) == True) and (('ipadx' in layout) == False) and (('ipady' in layout) == False):
      widget.pack(anchor=layout['anchor'], padx=layout['padx'], pady=layout['pady'])
    elif (('anchor' in layout) == False) and (('side' in layout) == True) and (('fill' in layout) == False) and (('expand' in layout) == False) and (('padx' in layout) == True) and (('pady' in layout) == True) and (('ipadx' in layout) == False) and (('ipady' in layout) == False):
      widget.pack(side=layout['side'], padx=layout['padx'], pady=layout['pady'])
    elif (('anchor' in layout) == True) and (('side' in layout) == True) and (('fill' in layout) == False) and (('expand' in layout) == False) and (('padx' in layout) == True) and (('pady' in layout) == True) and (('ipadx' in layout) == False) and (('ipady' in layout) == False):
      widget.pack(anchor=layout['anchor'], side=layout['side'], padx=layout['padx'], pady=layout['pady'])
    elif (('anchor' in layout) == True) and (('side' in layout) == True) and (('fill' in layout) == False) and (('expand' in layout) == True) and (('padx' in layout) == True) and (('pady' in layout) == True) and (('ipadx' in layout) == False) and (('ipady' in layout) == False):
      widget.pack(anchor=layout['anchor'], side=layout['side'], expand=layout['expand'], padx=layout['padx'], pady=layout['pady'])
    elif layout['type'] == 'menu' :
      pass
    else :
      widget.pack()
    return

  # grid レイアウト
  def __gridder(self, layout, widget) :
    if (('column' in layout) == True) and (('row' in layout) == True) and (('columnspan' in layout) == True) and (('rowspan' in layout) == True) and (('sticky' in layout) == True) and (('padx' in layout) == True) and (('pady' in layout) == True) and (('ipadx' in layout) == True) and (('ipady' in layout) == True) :
      widget.grid(column=layout['column'], row=layout['row'], columnspan=layout['columnspan'], rowspan=layout['rowspan'], sticky=layout['sticky'], padx=layout['padx'], pady=layout['pady'], ipadx=layout['ipadx'], ipady=layout['ipady'])
    elif (('column' in layout) == True) and (('row' in layout) == True) and (('columnspan' in layout) == False) and (('rowspan' in layout) == False) and (('sticky' in layout) == False) and (('padx' in layout) == False) and (('pady' in layout) == False) and (('ipadx' in layout) == False) and (('ipady' in layout) == False) :
      widget.grid(column=layout['column'], row=layout['row'])
    elif (('column' in layout) == True) and (('row' in layout) == True) and (('columnspan' in layout) == False) and (('rowspan' in layout) == False) and (('sticky' in layout) == True) and (('padx' in layout) == False) and (('pady' in layout) == False) and (('ipadx' in layout) == False) and (('ipady' in layout) == False) :
      widget.grid(column=layout['column'], row=layout['row'], sticky=layout['sticky'])
    elif (('column' in layout) == True) and (('row' in layout) == True) and (('columnspan' in layout) == True) and (('rowspan' in layout) == True) and (('sticky' in layout) == True) and (('padx' in layout) == False) and (('pady' in layout) == False) and (('ipadx' in layout) == False) and (('ipady' in layout) == False) :
      widget.grid(column=layout['column'], row=layout['row'], sticky=layout['sticky'], colspan=layout['colspan'], rowspan=layout['rowspan'])
    elif (('column' in layout) == True) and (('row' in layout) == True) and (('columnspan' in layout) == False) and (('rowspan' in layout) == False) and (('sticky' in layout) == False) and (('padx' in layout) == True) and (('pady' in layout) == True) and (('ipadx' in layout) == False) and (('ipady' in layout) == False) :
      widget.grid(column=layout['column'], row=layout['row'], padx=layout['padx'], pady=layout['pady'])
    elif (('column' in layout) == True) and (('row' in layout) == True) and (('columnspan' in layout) == False) and (('rowspan' in layout) == False) and (('sticky' in layout) == True) and (('padx' in layout) == True) and (('pady' in layout) == True) and (('ipadx' in layout) == False) and (('ipady' in layout) == False) :
      widget.grid(column=layout['column'], row=layout['row'], sticky=layout['sticky'], padx=layout['padx'], pady=layout['pady'])
    elif (('column' in layout) == True) and (('row' in layout) == True) and (('columnspan' in layout) == False) and (('rowspan' in layout) == False) and (('sticky' in layout) == False) and (('padx' in layout) == False) and (('pady' in layout) == False) and (('ipadx' in layout) == True) and (('ipady' in layout) == True) :
      widget.grid(column=layout['column'], row=layout['row'], ipadx=layout['ipadx'], ipady=layout['ipady'])
    elif (('column' in layout) == True) and (('row' in layout) == True) and (('columnspan' in layout) == False) and (('rowspan' in layout) == False) and (('sticky' in layout) == True) and (('padx' in layout) == False) and (('pady' in layout) == False) and (('ipadx' in layout) == True) and (('ipady' in layout) == True) :
      widget.grid(column=layout['column'], row=layout['row'], sticky=layouy['sticky'], ipadx=layout['ipadx'], ipady=layout['ipady'])
    else :
      widget.pack()
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
    elif key in cls.Keys_menu :
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

  # メッセージボックス
  def messageBox(self, message, mbtype="info") :
    a = False
    if mbtype == "info" :
      messagebox.showinfo("Information", message)
    elif mbtype == "error" :
      messagebox.showerror("Error", message)
    elif mbtype == "warning" :
      messagebox.showwarning("Warning", message)
    elif mbtype == "okcancel" :
      a = messagebox.askokcancel("isOK", message)
    elif mbtype == "question" :
      a = messagebox.askquestion("Question", message)
    elif mbtype == "retry" :
      a = messagebox.askretrycancel("Retry", message)
    else :
      pass
    return a

  # ファイル選択ダイアログを開く
  def fileDailog(self, initdir) :
    file = filedialog.askopenfile(filetypes=[("","*")], initialdir=initdir)
    if file == None :
      return ""
    else :
      return file.name

  # 子ウィンドウを作成する。
  def createWindow(parent, title, size, location=(0, 0)) :
    newwin = Toplevel(parent)
    newwin.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(size[0], size[1], location[0], location[1]))
    newwin.title(title)
    return newwin

  # ウィジェットの値を得る。
  def getWidgetValue(self, name) :
    rv = ""
    w = self.getWidget(name)
    if type(w) is tk.Entry :
      rv = w.get()
    elif type(w) is tk.Label:
      rv = w["text"]
    elif type(w) is ttk.Checkbutton or type(w) is ttk.Radiobutton:
      rv = True if w.state()[0] == "focus" else False
    elif type(w) is tk.Listbox :
      try :
        rv = w.curselection()[0]
      except :
        rv = -1
    else :
      pass
    return rv



    
'''  以下はインスタンス化の仕方の例
root = tk.Tk()
app = TkApp(master=root, filename="TkApp.json")
app.mainloop()
'''
