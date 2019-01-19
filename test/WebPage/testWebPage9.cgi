#!/usr/bin/env python3
# -*- code=utf-8 -*-
# WebPage クラスのテスト
#   echo() メソッド
import WebPage as page
import FileSystem as fs
import sys

class TestPage(page.WebPage) :
  # コンストラクタ
  def __init__(self, template="") :
    super().__init__(template)
    #self.vars['message'] = "バージョン：" + str(page.VERSION)
    #filePath = '/home/user/Pictures/graphics/LoveLive.jpg'
    #filePath = '/home/user/Pictures/graphics/home.png'
    filePath = '/home/user/Pictures/SVG/Android Activity.svg'
    #filePath = '/home/user/archives/data.zip'
    self.extension = fs.getExtension(filePath)
    self.loadFile(filePath)


# メイン開始位置
#wp = TestPage('templates/template9.html')
wp = TestPage()
wp.echo()
