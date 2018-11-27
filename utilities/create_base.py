#!/usr/bin/env python3
#  create application base.
import io, tarfile
from Py365Lib import Common, FileSystem as fs, Text as txt

# バージョン
VER = "1.00"

# INI ファイル
INI = "./create_base.ini"

basedir = ""  # アプリ作成先のディレクトリ
apptype = 0   # アプリ種別
appname = ""  # アプリ名

targz = "create_base_s.tar.gz"

# ユーザのアプリ情報入力
def input_appinfo() :
  global basedir
  global apptype
  global subtype
  global appname
  
  # INI ファイルがあれば読み込む。
  if fs.isFile(INI) :
    conf = fs.readIni(INI)
    basedir = conf['basedir']
    targz = conf['targz']
  else :
    basedir = Common.readline("アプリひな型を作成するディレクトリを指定してください。> ")

  # ひな型を作成するディレクトリがあるか確認
  if not fs.exists(basedir) :
    Common.stop(2, "構築先 " + basedir + " が存在しません。")

  # アプリ種別を得る。
  while True :
    apptype = Common.readline("\nアプリひな型の種別を入力してください。\nA: Console, C: CGI, T: Curses, H: HTTP Server, G: Tkinter > ")
    if apptype == 'A' or apptype == 'C' or apptype == 'T' or apptype == 'H' or apptype == 'G' :
      break
    else :
      Common.esc_print("red", "A, C, T, H, G のどれかを入力してください。\n")

  # アプリのサブ種別を得る。
  subtype = get_subtype(apptype)
  
  # アプリ名を得る。
  appname = Common.readline("\nアプリ名を入力してください。この名前はアプリのディレクトリ名になります。> ")
  return

# アプリのサブ種別を得る。
def get_subtype(atype:str) -> int:
  st = -1
  if atype == 'A' :
    st = 0
  elif atype == 'C' :
    pass
  elif atype == 'T' :
    pass
  elif atype == 'H' :
    pass
  elif atype == 'G' :
    pass
  else :
    pass
  return st

# ひな型作成
def create_app() :
  return

# アプリケーションの説明を返す。
def getAppTypeName(apptype) :
  result = "不明なタイプ"
  if apptype == 'A' :
    result = "コンソールアプリケーション (Common 使用)"
  elif apptype == 'C' :
    result = "CGI Web アプリケーション (WebPage 使用)"
  elif apptype == 'T' :
    result = "curses コンソールアプリケーション (CursesApp 使用)"
  elif apptype == 'H' :
    result = "簡易 HTTP サーバ (HTApp 使用)"
  elif apptype == 'G' :
    result = "GUI アプリケーション (TkApp 使用)"
  else :
    pass
  return result


# tar.gz ファイルからターゲットのファイルを取り出す。
def extract_file(targz, target) :
  #  tar.gz ファイルを開く
  tar = tarfile.open(targz)
  #  リーダを取得してファイルを読む。
  reader = tar.extractfile(target)
  buff = reader.read()
  # ターゲットに書き込む。
  with open(target, 'wb') as f :
    f.write(buff)
  # 閉じる。
  reader.close()
  tar.close()
  return


#  
#  Main 開始
#  ~~~~~~~~~~
if  __name__ == "__main__" :
  # タイトル表示
  Common.esc_print("green", "Py365Lib アプリひな型作成ツール version " + VER)
  # 情報入力
  while True :
    try :
      input_appinfo()
      Common.esc_print("yellow", "\n{0}/{1} に {2} のアプリひな型を作成します。(Y/N) > ".format(basedir, appname, getAppTypeName(apptype)))
      a = input()
      if txt.toupper(a) == "Y" :
        break
      else :
        Common.stop(1, "アプリひな型の作成を中止しました。")
    except KeyboardInterrupt :
      Common.stop(3, "\nユーザにより中断されました。\n")
      
  # ひな型作成
  try :
    create_app()
    Common.esc_print("bold", "\nな型の作成に成功しました。")
  except Exception as e :
    Common.esc_print("red", e.message)

  
