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
contlist = {} # ひな形一覧
files = []    # コピーするファイル

targz = "create_base.tgz"

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
  else :
    Common.esc_print("green", "アプリケーションは {0} に作成されます。これを変更するには、AppConf.ini を編集します。".format(basedir))

  # アプリ種別を得る。
  while True :
    apptype = Common.readline("\nアプリひな型の種別を入力してください。(大文字で指定します)\nA: Console, C: CGI, T: Curses, H: HTTP Server, G: Tkinter, X: 中断 > ")
    if apptype == 'A' or apptype == 'C' or apptype == 'T' or apptype == 'H' or apptype == 'G' :
      break
    elif apptype == 'X' :
      Common.stop(9, "中断しました。")
    else :
      Common.esc_print("red", "A, C, T, H, G のどれかを入力してください。\n")

  # アプリのサブ種別を得る。
  subtype = get_subtype(apptype)
  
  # アプリ名を得る。
  appname = Common.readline("\nアプリ名を入力してください。この名前はアプリのディレクトリ名になります。> ")
  return

# アプリのサブ種別を得る。
def get_subtype(atype:str) -> int:
  n = -1
  if atype == 'A' :
    # contlist のキー "A?"
    print("1 基本のコンソールアプリケーション")
    print("2 ログあり、ファイル一括読み込み処理")
    print("3 ログあり、ファイル行単位読み込み処理")
    print("4 ログなし、INI ファイル読み込み")
    s = Common.readline("番号を入力してください。")
    n = int(s) - 1
  elif atype == 'C' :
    # contlist のキー "C?"
    print("1 基本の CGI")
    print("2 フォームとクッキー")
    print("3 MySQLを使用する")
    print("4 ファイルアップロード")
    print("5 リダイレクト")
    print("6 Ajax get text")
    print("7 Ajax get JSON")
    print("8 Ajax get image")
    print("9 ォームと各種コントロール")
    s = Common.readline("番号を入力してください。")
    n = int(s) - 1
  elif atype == 'T' :
    # contlist のキー "T?"
    print("1 基本の curses アプリケーション")
    print("2 リソースファイルを使った Form")
    print("3 オーバーライドメソッドを使った Form")
    s = Common.readline("番号を入力してください。")
    n = int(s) - 1
  elif atype == 'H' :
    # contlist のキー "H?"
    print("1 基本の簡易 HTTP サーバ")
    print("2 フォームを利用する")
    print("3 Ajax")
    s = Common.readline("番号を入力してください。")
    n = int(s) - 1
  elif atype == 'G' :
    # contlist のキー "G?"
    print("1 基本の Tk アプリケーション")
    print("2 フォーム")
    print("3 メニュー")
    print("4 ウィンドウ")
    s = Common.readline("番号を入力してください。")
    n = int(s) - 1
  else :
    pass
  return n


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


# tgz ファイルからターゲットのファイルを取り出す。
def extract_file(targz, src, dest) :
  #  tar.gz ファイルを開く
  tar = tarfile.open(targz)
  #  リーダを取得してファイルを読む。
  reader = tar.extractfile(src)
  buff = reader.read()
  # 書き込み先ファイルの親フォルダが存在しない場合は作成する。
  parent = fs.getParentDirectory(dest)
  if not fs.exists(parent) :
    fs.mkdir(parent)
  # ターゲットに書き込む。
  fs.writeBinary(dest, buff)
  # 閉じる。
  reader.close()
  tar.close()
  return


# tgz から index.csv を取り出して contlist に格納
def create_contlist() :
  global contlist
  global files
  global targz
  #  tar.gz ファイルを開く
  tar = tarfile.open(targz)
  #  リーダを取得してファイルを読む。
  reader = tar.extractfile('create_base/index.csv')
  buff = reader.read()
  s = Common.from_bytes(buff)
  # 内容を contents に保存
  contlist.clear()
  files.clear()
  lines = txt.split("\n", s)
  for line in lines :
    kv = txt.split(",", line)
    if len(kv) >= 2 :
      key = kv[0]
      files.append([key])
      files1 = files[len(files) - 1]
      contlist[key] = kv[1]
      # コピーするファイル名を files に設定する。
      if len(kv) >= 3 :
        for i in range(2, len(kv)) :
          files1.append(kv[i])
  return


# ひな型作成
def create_app(key) :
  global targz
  b = False
  # フォルダ作成
  place = basedir + "/" + appname
  if fs.exists(place) :
    a = Common.readline("{0} はすでに存在します。上書きしますか？ (Y/N)".format(place))
    if a != "Y" :
      return False
  else :
    fs.mkdir(place)
  # コピーするファイルリストを探す。
  for row in files :
    if row[0] == key :
      # ファイルをコピーする。
      for i in range(1, len(row)) :
        target = row[i]
        dest = place + "/" + target
        src = "create_base/" + target
        extract_file(targz, src, dest)
      b = True
      break
    else:
      pass
  return b



#
#  Main 開始
#  ~~~~~~~~~~
if  __name__ == "__main__" :
  # コマンドライン引数でINIファイルを指定しているか？
  if Common.count_args() > 0 :
    INI = Common.args()[0]
  # タイトル表示
  Common.esc_print("green", "Py365Lib アプリひな型作成ツール version " + VER)
  # ひな形リスト (contlist) 作成
  create_contlist()

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
    if create_app(apptype + str(subtype)) :
      Common.esc_print("bold", "\nひな型の作成に成功しました。")
    else :
      Common.stop(5, "\nエラーによりひな型の作成に失敗しました。")
  except Exception as e :
    Common.esc_print("red", e.message)
