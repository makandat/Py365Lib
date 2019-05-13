# -*- coding: utf-8 -*-
# CSS3 クラス  Version 1.0  2019-05-12

VERSION   = "1.0"


# クラス
class CSS3 :
  
  # コンストラクタ
  def __init__(self, presets=None) :
    self.lines = []
    if presets != None :
      self.lines.extend(presets)
    return

  # 他のCSS3オブジェクトを結合する。
  def append(self, css) :
    self.lines.expand(css)
    return

  # 任意の CSS をそのまま追加する。
  def literal(self, css) :
    self.lines.append(css)
    return

  # 文字列に変換する。
  def tostring(self, withtag=False) :
    if withtag :
      s = "<style>\n"
    s += "\n".join(self.lines)
    if withtag :
      s += "<style>\n"
    return s

  # ファイル保存
  def save(self, filePath, withtag=False) :
    s = self.tostring(withtag)
    with open(filePath, "w", encoding="utf-8") as f :
      f.write(s)
    return

  # オブジェクトのスタイル定義開始
  def begin_object(self, obj) :
    self.lines.append(obj + " {\n")
    return

  # オブジェクトのスタイル定義終わり
  def end_object(self) :
    self.lines.append("}\n")
    return

  # 影(箱)
  #   obj: 対象のセレクタ
  #   distances: [dx, dy[, blur, [spread]]]
  #      水平方向の影のオフセット距離, 垂直方向の影のオフセット距離, ぼかし距離, 広がり距離
  #   color: 色
  #   inset: 影を内側に付ける。
　def box_shadow(self, distances, color=None, inset=False) :
    s += "box-shadow: "
    for d in distances :
      s += d
      s += " "
    if color != None :
      s += color
    else :
      pass
    if inset :
      s += " inset\n"
    else
      pass
    s += ";"
    self.lines.append(s)
    return s

  # 影(テキスト)
  #   obj: 対象のセレクタ
  #   distances: [dx, dy]  影の水平と垂直距離
  #   radius: 影のぼかし半径
  #   color: 影の色
　def text_shadow(self, distances, radius=None, color=None) :
    s = "text-shadow: "
    s += distances[0] + " "
    s += distances[1]
    if radius != None :
      s += f" {radius}"
    if color != None :
      s += f" {color}"
    s += ";"
    self.lines.append(s)
    return s

  # 境界線
  def border(self, color, style, width) :
    s = "border :"
    s += "{0} {1} {2}".format(color, style, width)
    s += ";"
    self.lines.append(s)
    return

  # 境界線まるめ
  def border_radius(self, radius) :
    s = "border-radius :"
    for r in radius :
      s += r
      s += " "
    s1 = s.strip() + ";"
    self.lines.append(s1)
    return s1
    
  # 縁取り
  def outline(self, color, style, width) :
    s = "outline: "
    s += "{0} {1} {2}\n".format(color, style, width)
    s += ";"
    self.lines.append(s)
    return s

  # 背景：濃淡の変化
  def liner_gradation(self, colors, deg=None) :
    if deg == None :
      s = "background: liner-gradient({0}, {1});".format(colors[0], colors[1])
    else :
      s = "background: liner-gradient({0}, {1}, {2});".format(deg, colors[0], colors[1])
    self.lines.append(s)
    return s

  # 背景：円や楕円の濃淡の変化
  def radial_gradation(self, colors, size="closest-side", ellipse=False) :
    if ellipse :
      if len(colors) == 3 :
        s = "background: radial-gradient(ellipse {0}, {1}, {2}, {3});".format(size, colors[0], colors[1], colors[2])
      else :      
        s = "background: radial-gradient(ellipse {0}, {1}, {2});".format(size, colors[0], colors[1])
    else :
      if len(colors) == 3 :
        s = "background: radial-gradient(circle {0}, {1}, {2}, {3});".format(size, colors[0], colors[1], colors[2])
      else :
        s = "background: radial-gradient(circle {0}, {1}, {2});".format(size, colors[0], colors[1])
    self.lines.append(s)
    return s

  # 背景：画像
  def image(self, url) :
    s = "background-image: url({0});"
    self.lines.append(s)
    return s
    
  # 変形
  #  1番目の数値は、水平方向の縮尺（a）
  #  2番目の数値は、垂直方向の傾斜率（b）
  #  3番目の数値は、水平方向の傾斜率（c）
  #  4番目の数値は、垂直方向の縮尺（d）
  #  5番目の数値は、水平方向の移動距離（e）
6番目の数値は、垂直方向の移動距離（f）
  def transform(self, a, b, c, d, e) :
    s = "transform: matrix({0}, {1}, {2}, {3}, {4});}".format(a, b, c, d, e)
    self.lines.append(s)
    return s

  # 回転
  def rotate(self, deg) :
    s = "rotation: {0}deg;".format(deg)
    self.lines.append(s)
    return s


