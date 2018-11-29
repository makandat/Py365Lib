#!/usr/bin/env python3
#  画像を返す。
import WebPage as page
import os

class MyPage(page.WebPage) :
  IMGDIR = '/var/www/html/img'

  def __init__(self) :
    super().__init__(self)
    files = os.listdir(MyPage.IMGDIR)
    img = int(self.params['img'].value)
    path = MyPage.IMGDIR + "/" + files[img]
    MyPage.sendImage(path)

MyPage()

