#!/usr/bin/env python3
# -*- code=utf-8 -*-
# WebPage クラスのテスト
import WebPage as page

class TestPage(page.WebPage) :
  # コンストラクタ
  def __init__(self, template) :
    super().__init__(template)
    self.vars['message'] = "メッセージです。"
    if 'text1' in self.params :
        self.vars['message'] = self.params['text1']
    else :
        self.vars['message'] = "No paramter text1"

wp = TestPage('template.html')
wp.echo()
