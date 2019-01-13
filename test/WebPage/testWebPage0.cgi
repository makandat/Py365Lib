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
    if self.isParam('text1') :
        self.vars['message'] = self.getParam('text1')
    else :
        self.vars['message'] = fs.getCurrentDirectory()

# メイン開始位置
wp = TestPage('templates/template.html')
wp.echo()
