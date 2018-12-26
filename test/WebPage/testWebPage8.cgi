#!/usr/bin/env python3
# -*- code=utf-8 -*-
# WebPage クラスのテスト
#   クッキー
import WebPage as page
import FileSystem as fs

class TestPage(page.WebPage) :
  # コンストラクタ
  def __init__(self, template) :
    super().__init__(template)
    if 'count' in self.cookies :
        c = int(self.cookies['count'].value)
        c += 1
        self.cookie('count', str(c))
        self.vars['count'] = str(c)
    else :
        self.vars['count'] = '0'
        self.cookie('count', '0')

# メイン開始位置
wp = TestPage('templates/template8.html')
wp.echo()
