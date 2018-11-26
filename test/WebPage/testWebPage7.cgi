#!/usr/bin/env python3
# -*- code=utf-8 -*-
# WebPage クラスのテスト (7)
#   TextArea, Select, CheckBox, Radio
import WebPage as page
import os

class TestPage(page.WebPage) :
  # コンストラクタ
  def __init__(self, template) :
    super().__init__(template)
    if 'text1' in self.params :
        self.vars['message'] = self.getValues()
    else :
        self.vars['message'] = os.getcwd()

  # コントロールの値を得る。
  def getValues(self) :
    buff = ""
    buff += page.WebPage.tag('pre', self.params['text1'].value)
    buff += page.WebPage.tag('p', "Select1 = " + self.params['select1'].value)
    buff += page.WebPage.tag('p', "Check1 = " + self.params['check1'].value if 'check1' in self.params.keys() else 'Check1 is not checked')
    buff += page.WebPage.tag('p', "Radio1 = " + self.params['radio1'].value)
    return buff

# メイン開始位置
wp = TestPage('templates/template7.html')
wp.echo()
