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
    if self.isParam('text1') :
        self.vars['message'] = self.getValues()
    else :
        self.vars['message'] = os.getcwd()

  # コントロールの値を得る。
  def getValues(self) :
    buff = ""
    buff += page.WebPage.tag('pre', self.getParam('text1'))
    buff += page.WebPage.tag('p', "Select1 = " + self.getParam('select1'))
    buff += page.WebPage.tag('p', "Check1 = " + self.getParam('check1') if self.isParam('check1') else 'Check1 is not checked')
    buff += page.WebPage.tag('p', "Radio1 = " + self.getParam('radio1'))
    return buff

# メイン開始位置
wp = TestPage('templates/template7.html')
wp.echo()
