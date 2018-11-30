#!/usr/bin/env python3
# -*- code=utf-8 -*-
# WebPage クラスのテスト(5)
#   Ajax getJson
import WebPage as page

class TestPage(page.WebPage) :
  # コンストラクタ
  def __init__(self, template) :
    super().__init__(template)
    self.params['message'] = ''

# メイン開始位置
wp = TestPage('templates/template6.html')
wp.echo()