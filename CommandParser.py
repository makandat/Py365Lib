import json
import Common

# コマンドパーサ
class Parser :
  # コンストラクタ
  def __init__(self, params=None) :
    self.variables = []
    self.options = {}
    self.optval = False
    if params :
      for i, a in enumerate(params) :
        if a.startswith('"') and a.endswith('"') :
          a = a[1:-1]
        self.add(a, (i == len(params)))
    else :
      pass
    return

  # コマンドパラメータを追加
  def add(self, arg, last=False) :
    if arg.startswith('-') :
      self.opt = arg[1:]
      self.options[self.opt] = None
      self.optval = True
    elif self.optval :
      self.options[self.opt] = arg
      self.optval = False
    elif last :
      if self.options[self.opt] != None :
        self.variables.append(self.options[self.opt])
        self.options[self.opt] = None
    else :
      self.variables.append(arg)
    return

  # 現在の内容をダンプする。
  def dump(self) :
    vars = json.dumps(self.variables)
    opts = json.dumps(self.options)
    print(vars)
    print(opts)
    return
