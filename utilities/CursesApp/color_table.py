#!/usr/bin/env python3
#  カラーテーブル
from CursesApp import CursesApp

#
# アプリケーションクラス
#
class ColorTableApp(CursesApp) :
  # コンストラクタ
  def __init__(self) :
    super().__init__()

  # キー入力ハンドラ
  def handler(self, key) :
    return False

  # 初期表示
  def init_app(self) :
    # カラーテーブルの内容を表示する。
    self.__show_colors()

  # カラーテーブルの内容を表示する。
  def __show_colors(self) :
    self.print("カラーテーブルの内容 COLOR_PAIRS=" + str(self.MaxColorNumber), 10, 0, 1, CursesApp.UNDERLINE)
    for color in range(1, 17) :
      self.print("color=" + str(color), 10, color + 1, color)
      for color in range(17, 33) :
        self.print("color=" + str(color), 25, color - 15, color)
    self.hideCursor()

# ColorTableApp クラスをインスタンス化して開始
ColorTableApp()
