#!/usr/bin/env python3
#  複素数の極形式変換
import WebPage as page
import cmath

class MyPage(page.WebPage) :
  def __init__(self) :
    super().__init__(self)
    z = complex(self.params['complex'].value)
    pz = cmath.polar(z)
    json = "[" + str(pz[0]) + "," + str(pz[1]) + "]"
    MyPage.sendJson(json)    

MyPage()

