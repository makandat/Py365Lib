# -*- code=utf-8 -*-
# Version 1.10  2019-01-14
from typing import List, Tuple
import re

# 文字列のリスト
StrList = List[str]
StrTuple = Tuple[str]

# テキストクラス
class Text :
    # コンストラクタ
    def __init__(self, s:str="") :
        self.__text = s

    # 文字列の長さ
    @property
    def length(self) -> int:
        return len(self.__text)

    # インスタンスメソッド
    def append(self, s:str) ->str:
        self.__text += s
    
    # start から長さ length の部分文字列を返す。
    def substring(self, start:int, length:int) ->str:
        return self.__text[start:start+length]

    # start から end までの部分文字列を返す。
    def substr(self, start:int, end:int) ->str:
        return self.__text[start:end+1]

    # 先頭から長さ length の部分文字列を返す。
    def left(self, length:str) -> str:
        return self.__text[0:length]

    # 最後から長さ length の部分文字列を返す。
    def right(self, length:int) -> str:
        return self.__text[self.length-length:self.length]

    # このオブジェクトの文字列を返す。
    def toString(self) -> str:
        return self.__text

    # 文字列 c を n 回繰り返した文字列をこのオブジェクトの値とする。
    def times(self, c:str, n:int) -> str:
        self.__text = c * n

    # このオブジェクトの文字列をクリアする。
    def clear(self) :
        self.__text = ""

# 数字を判別
def isdigit(a: str) -> str:
  return a.isdigit()

# アルファベットを判別
def isalpha(a: str) -> str:
  return a.isalpha()

# 区切りを判別
def isdelim(a: str) -> str:
  return not a.isalnum()

# 表示可能かを判別
def isprint(a:str) ->bool:
  return a.isprintable()

# 小文字に変換
def tolower(s:str) -> bool:
  return s.lower()

# 大文字に変換
def toupper(s: str) -> bool:
  return s.upper()

# 前後の空白を取り除く
def trim(s: str) -> str:
  return s.strip()

# 後ろのCRやLFを取り除く
def chomp(s: str) -> str:
  if len(s) < 2 :
    return s
  last = len(s) - 1
  if s[last] == '\n' or s[last] == '\r' :
    s = s[0:last]
    last -= 1
    if s[last] == '\r' :
      s = s[0:last]
  return s

# 文字 c で文字列 s を分割してリストとして返す。
def split(c:bytes, s:str) -> StrList:
  return s.split(c)

# リスト array の要素を文字 c で連結する。
def join(c:str, array:StrList) -> str:
  return c.join(array)

# 文字列 s の中に部分文字列 p が含まれているか判別する。
def contain(p:str, s:str) -> bool:
  return (p in s)

# 文字列 s の中に部分文字列 p が含まれていればその位置を返す。
def indexOf(p:str, s:str) -> int:
  return s.find(p)

# 文字列 s に部分文字列 old が含まれていれば、それを new に置き換える。
def replace(old:str, new:str, s:str) -> str:
  return s.replace(old, new)

# 書式を含む文字列 form を *args (可変個数のパラメータ) で置き換える。
def format(form:str, *args: StrTuple) :
 return form.format(*args)

# 文字列 s を整数に変換する。
def parseInt(s:str) -> int:
 return int(s)

# 文字列 s を浮動小数点数に変換する。
def parseDouble(s:str) -> float:
 return float(s)

# 256未満の整数を文字に変換する。
def char(n:int) -> str:
 return chr(n)

# 文字を256未満の整数に変換する。
def asc(a:str) -> int:
  return ord(a)

#    正規表現を使う静的メソッド
# 正規表現 rstr が文字列 s に含まれるか判別する。
def re_contain(rstr:str, s:str) -> bool :
  ro = re.compile(rstr)
  m = ro.match(s)
  return m != None

# 正規表現 rstr が文字列 s に含まれていれば、その一致した部分文字列の集合を返す。
def re_search(rstr:str, s:str) -> re.match :
  ro = re.compile(rstr)
  m = ro.search(s)
  return m

# 正規表現 rstr が文字列 s に含まれていれば、その部分文字列で分割してリストとして返す。
def re_split(rstr:str, s:str) -> StrList :
  m = re.split(rstr, s)
  return m

# 正規表現 rstr が文字列 s に含まれていれば、その部分文字列を c で置き換える。
def re_replace(rstr:str, c:str, s:str) -> str :
  ro = re.compile(rstr)
  return ro.sub(c, s)


# --- v1.03 で追加 ---

# 数(整数または浮動小数点数) d に3桁ごとにカンマを挿入した文字列を返す。
def money(d:float) -> str :
  m = '{0:,}'.format(d)
  return m


# --- v1.10 で追加 ---

# 部分文字列を得る。(長さを指定)
def substring(s:str, start:int, length:int) -> str :
  n = len(s)
  end = start + length
  if end >= n :
    return s[start:n]
  else :
    return s[start:end]

# 部分文字列を得る。(位置を指定)
def substr(s:str, start:int, end:int) -> str :
  if end <= start :
    return ""
  n = len(s)
  if end >= n :
    return s[start:n]
  else :
    return s[start:end + 1]

# 部分文字列を得る。(左側 n 文字)
def left(s:str, n:int) -> str :
  if n >= len(s) :
    return s
  else :
    return s[0 : n]

# 部分文字列を得る。(右側 n 文字)
def right(s:str, n:int) -> str :
  if n > len(s) :
    return s
  else :
    leng = len(s)
    return s[leng - n : leng]

# 部分文字列が含まれる回数を返す。
def str_count(s:str, sub:str) -> int :
  return s.count(sub)
