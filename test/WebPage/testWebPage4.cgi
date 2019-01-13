#!/usr/bin/env python3
# -*- code=utf-8 -*-
# WebPage クラスのテスト (4)
#   Ajax getText
import WebPage as page

class TestPage(page.WebPage) :
  # コンストラクタ
  def __init__(self, template) :
    super().__init__(template)
    self.vars['message'] = ''

# メイン開始位置
wp = TestPage('templates/template4.html')
wp.echo()
