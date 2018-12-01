#!/usr/bin/env python3
# -*- code=utf-8 -*-
# WebPage クラスのテスト
#   フォームとクッキー
import WebPage as page
import FileSystem as fsys
# import os

class TestPage(page.WebPage) :
  # コンストラクタ
  def __init__(self, template) :
    super().__init__(template)
    if 'text1' in self.params :
        self.vars['message'] = self.params['text1'].value + "<br />\n"
    else :
        self.vars['message'] = fsys.getCurrentDirectory() + "<br />\n"  # os.getcwd()
    self.cookie('key1', 'value1')
    if 'key1' in self.cookies :
        self.vars['message'] += (" cookie key1=" + self.cookies['key1'])

# メイン開始位置
wp = TestPage('templates/C1.html')
wp.echo()
