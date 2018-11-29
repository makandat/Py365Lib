#!/usr/bin/env python3
#  CursesApp クラスを利用したサンプル
from CursesApp import CursesApp

class CApplication(CursesApp) :
  # コンストラクタ
  def __init__(self) :
    super().__init__()

  # オーバーライド (初期表示)
  def init_app(self) :
    self.print("CursesApp サンプル")

# Start
CApplication()
