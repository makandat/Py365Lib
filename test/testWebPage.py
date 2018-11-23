#!/usr/bin/env python3
# -*- code=utf-8 -*-
# WebPage クラスのテスト
import WebPage as page

class TestPage(page.WebPage) :
  # コンストラクタ
  def __init__(self, template) :
    super().__init__(template)
    if 'text1' in self.params :
        self.vars['message'] = self.params['text1']
    else :
        self.vars['message'] = 'メッセージです。text1 is null.'
    self.cookie('key1', 'value1')
    if 'key1' in self.cookies :
        self.vars['message'] += (" cookie key1=" + self.cookies['key1'])

# メイン開始位置
wp = TestPage('template.html')
wp.echo()
