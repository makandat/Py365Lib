# -*- coding: utf-8 -*-
# JQuery クラス  Version 1.0  2019-05-12

VERSION   = "1.0"


# クラス
class JQuery :
  
  # コンストラクタ
  def __init__(self, cdnver="3.4.1") :
    self.lines = []
    if cdnver == "" or cdnver == None :
      pass
    else :
      self.lines.append("<script src=\"https://code.jquery.com/jquery-{0}.min.js\"></script>".format(cdnver))
    self.lines.append("<script>")
    self.lines.append(" $(function() {")
    return

  # イベントハンドラのグループを終わりにする。
  def close_events(self) :
    self.lines.append("});")
    return

  # 文字列に変換する。
  def tostring() :
    s = ""
    s += "\n".join(self.lines)
    s += "</script>\n"
    return s

  # ファイル保存する。
  def save(self, filePath) :
    return

  # 文字列をそのままコードのリストに追加する。
  def literal(self, code) :
    self.lines.append(code)
    return

  #  コントロールイベント
  def control(self, selector_name, selector_type="id", event="click") :
    prefix = ""
    if selector_type == 'id' :
      prefix = "#"
    elif selector_type == 'class' :
      prefix = '.'
    else :
      pass
    s = "$(\"{0}{1}\").".format(prefix, selector_name)
    s += "{0}(function(){".format(event)
    s += "  // todo: ここにイベントハンドラのコードを追加する。"
    s += "});"
    self.lines(s)
    return s

  #  Ajax で URL からデータを取得
  def ajax_get(self, url, parameters, id=None) :
    s = "$.get({0}, {1}, function(data) {".format(url, parameters)
    if id == None :
      s += "  // todo: ここにデータを受け取ったときのコードを追加する。"
    else :
      s += "  $("#{0}").text(data);".format(id);
    s += "});"
    return

  #  Ajax で URL へフォームデータをポスト
  def ajax_post(self, url, parameters, id) :
    s = "$.post({0}, {1}, function(data) {".format(url, parameters)
    if id == None :
      s += "  // todo: ここにデータを受け取ったときのコードを追加する。"
    else :
      s += "  $("#{0}").text(data);".format(id);
    s += "});"
    return

    
