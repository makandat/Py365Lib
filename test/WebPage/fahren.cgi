#!/usr/bin/env python3
#  華氏温度と摂氏温度変換
import WebPage as page

class MyPage(page.WebPage) :
  def __init__(self) :
    super().__init__(self)
    t = float(self.params['text1'].value)
    fahren = self.params['temp'].value
    if fahren == 'F' :
      # 華氏温度へ
      self.ct = 9.0 * t / 5.0 + 32.0
    else :
      # 摂氏温度へ
      self.ct = 5.0 * (t - 32.0) / 9.0
    MyPage.sendText(str(self.ct))    

MyPage()

