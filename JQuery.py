# -*- coding: utf-8 -*-
# JQuery クラス  Version 1.01  2019-07-24
import FileSystem as fs
VERSION   = "1.01"


# クラス
class JQuery :
  
  # コンストラクタ
  def __init__(self, cdnver="3.4.1") :
    self.lines = []
    self.literals = []
    self.cdnver = cdnver
    return

  # イベントハンドラのグループを終わりにする。
  def close_events(self) :
    self.lines.append("});")
    return

  # 文字列に変換する。
  def tostring(self) :
    s = ""
    if not (self.cdnver == "" or self.cdnver == None) :
      s += "<script src=\"https://code.jquery.com/jquery-{0}.min.js\"></script>".format(self.cdnver)
    s += "\n<script>\n"
    if len(self.lines) > 0 :
      s += " $(function() {\n"
      s += "\n".join(self.lines)
      s += "});\n";
    if len(self.literals) > 0 :
      s += "\n".join(self.literals)
    s += "\n</script>\n"
    return s

  # ファイル保存する。
  def save(self, filePath) :
    fs.writeAllText(filePath, self.tostring())
    return

  # 文字列をそのままコードのリストに追加する。
  def literal(self, code) :
    self.literals.append(code)
    return

  #  コントロールイベント
  def event_handler(self, selector_name, selector_type="id", event="click", code="\n") :
    prefix = ""
    if selector_type == 'id' :
      prefix = "#"
    elif selector_type == 'class' :
      prefix = '.'
    else :
      pass
    s = "  $(\"{0}{1}\").".format(prefix, selector_name)
    s += "{0}(function()".format(event) + "{\n"
    s += code
    s += "  });\n"
    self.lines.append(s)
    return s

  #  Ajax で URL からデータを取得
  def ajax_get(self, url, parameters, json=False, id=None, code="") :
    if json :
      s = "  $.getJSON(\"{0}\", {1}, function(data) ".format(url, parameters) + "{\n"
    else :
      s = "  $.get(\"{0}\", {1}, function(data) ".format(url, parameters) + "{\n"
    if id == None or id == "":
      s += code
    else :
      s += " 　 $(\"#" + id + "\").text(data);"
    s += "\n  });\n"
    self.lines.append(s)
    return s

  #  Ajax で URL へフォームデータをポスト
  def ajax_post(self, url, parameters, id, code="") :
    s = "  $.post(\"{0}\", {1}, function(data) ".format(url, parameters) + "{\n"
    if id == None or id == "":
      s += code
    else :
      s += "   $(\"#{0}\").text(data);".format(id);
    s += "\n   });\n"
    self.lines.append(s)
    return s

    
