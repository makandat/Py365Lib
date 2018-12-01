#!/usr/bin/env python3
# -*- code=utf-8 -*-
# WebPage クラスのテスト(5)
#   Ajax getJSON
import WebPage as page

class TestPage(page.WebPage) :
  # コンストラクタ
  def __init__(self, template) :
    super().__init__(template)
    self.vars['message'] = ''

# メイン開始位置
wp = TestPage('templates/C6.html')
wp.echo()
