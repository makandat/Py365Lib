#!/usr/bin/env python3
import sys
from Py365Lib import *

# esc_print 関数を使うと簡単に表示属性を変更できる。
Common.esc_print(Common.ESC_FG_GREEN, sys.argv[0])
Common.esc_print(Common.ESC_UNDERLINE, sys.argv[0])

# 直接、エスケープシーケンスを使うと、属性を組み合わせて使える。
print(Common.ESC_FG_CYAN + Common.ESC_BG_BLUE + Common.ESC_BLINK + "Complex Escape Sequence" + Common.ESC_NORMAL)

# ESC_NOMRAL でもとに戻ったか確認
print("Reset")
