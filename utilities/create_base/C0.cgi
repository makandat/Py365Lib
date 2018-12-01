#!/usr/bin/env python3
# Hello, world!
import WebPage as page
import FileSystem as fsys
# import os

class Hello(page.WebPage) :
  # コンストラクタ
  def __init__(self, template) :
    super().__init__(template)
    self.vars['message'] = "Hello, world!"

# メイン開始位置
wp = Hello('templates/C0.html')
wp.echo()
