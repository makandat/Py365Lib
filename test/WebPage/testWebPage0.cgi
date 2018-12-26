#!/usr/bin/env python3
# -*- code=utf-8 -*-
# WebPage クラスのテスト
#   フォーム
import WebPage as page
import FileSystem as fs
# import os

class TestPage(page.WebPage) :
  # コンストラクタ
  def __init__(self, template) :
    super().__init__(template)
    if 'text1' in self.params :
        self.vars['message'] = self.params['text1'].value
    else :
        self.vars['message'] = fs.getCurrentDirectory()

# メイン開始位置
wp = TestPage('templates/template.html')
wp.echo()
