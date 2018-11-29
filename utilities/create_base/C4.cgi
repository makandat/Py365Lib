#!/usr/bin/env python3
# -*- code=utf-8 -*-
# WebPage クラスのテスト (3)
#   リダイレクト 
import WebPage as page

class TestPage(page.WebPage) :
  # コンストラクタ
  def __init__(self, template) :
    super().__init__(template)
    if 'text1' in self.params :
        #self.vars['message'] = self.params['text1'] + "<br />\n"
        self.redirect(self.params['text1'])
    else :
        self.vars['message'] = "指定URLへジャンプします。"

# メイン開始位置
wp = TestPage('templates/template3.html')
wp.echo()
