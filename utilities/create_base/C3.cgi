#!/usr/bin/env python3
# -*- code=utf-8 -*-
# WebPage クラスのテスト (2)
#   ファイルアップロード
import WebPage as page
import FileSystem as fsys

class TestPage(page.WebPage) :
  # コンストラクタ
  def __init__(self, template) :
    super().__init__(template)
    if 'file1' in self.params.keys() :
      self.saveFile('file1', '/var/www/data')
      file1 = self.params['file1']
      self.vars['message'] = 'アップロードOK　' + file1.filename
    else :
      self.vars['message'] = 'ファイルを指定してください。'

# メイン開始位置
wp = TestPage('templates/C3.html')
wp.echo()
