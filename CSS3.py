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

  # 任意の CSS をそのまま追加する。
  def literal(self, css) :
    self.lines.append(css)
    return

  # 影
　def shadow(self) :
    return

  # 縁取り
  def outline(self) :
    return

  # 照明
  def gradient(self) :
    return

  # 変形
  def transform(self) :
    return

  # 回転
  def rotate(self) :
    return

  # 文字飾り
  def decoration(self) :
    return
