#!/usr/bin/env python3
#  version 1.00  2018-12-28
import os, sys, io
import http.server
import http.cookies
import urllib.parse
from pprint import pprint
from syslog import syslog

PORT = 3330
SERVER_NAME = ''
STATIC = "./html"
TEMPLATES = "./templates"

# リクエスト対ハンドラのリスト
routes = {}
# 外部からくるパラメータ
params = {}
# クッキー
cookies = {}
# 動的な埋め込み変数
vars = {}
# POST のときの読み込み先
posted_file = io.BufferedIOBase()

# 設定ファイルを読む。
def readConf(filename="AppConf.ini") :
  result = {}
  if os.path.exists(filename) == False :
    return {"server_name":SERVER_NAME, "port":PORT}
  else :
    with open(filename) as f:
      for line in f :
        line = line.strip()
        if len(line) == 0 :
          pass
        elif line[0] == '#' or line[0] == '[':
          pass
        else :
          kv = line.split('=')
          result[kv[0].strip()] = kv[1].strip()
  return result

# リクエストに対応する HTML, JSON, TEXT を返す。
#   戻り値はタプル (type, content)
#   HTApp クラス内部で使用する。
def getContent(path, post=False) :
  # ルートが見つからない場合のエラーページを定義する。
  HTML = '''<html>
<head>
 <meta charset="utf-8" />
 <title>HTApp1</title>
 <style>
  body {
    margin-left: 5%;
    margin-right: 5%;
  }
  h1 {
    padding: 8px;
    color: crimson;
  }
  a:link, a:visited {
    color: blue;
    text-decoration: none;
  }
 </style>
</head>
<body>
 <h1>HTApp</h1>
 <p>エラー：不明なリクエスト ((*route*)) です。<a href="/">( "/" へもどる)</a></p>
 <p>(*path*)</p>
</body>
</html>'''
  # パスのうちルート部分を取得
  route = path
  try :
    n = path.index('?')
    route = path[0:n]
  except :
    pass
  # ルートのコレクションに route が含まれているか？
  if route in routes.keys() :
    # 含まれる場合は、そのハンドラをコールする。
    (type, content) = routes[route](path)
  else :
    # 含まれない場合は、エラーページを表示
    content = HTML.replace("(*path*)", path)
    content = content.replace("(*route*)", route)
    type = "text/html"
  return (type, content.encode('utf-8'))

# HTML タグを作成する。
def tag(tagname, text, attr="") :
  s = ""
  if attr == "" :
    s += "<" + tagname + ">"
  else :
    s += "<" + tagname + " " + attr + ">"
  s += text
  s += "</" + tagname + ">\n"
  return s

# 動的な埋め込み変数を HTML に埋め込む。
def embed(html) :
  for key in vars.keys() :
    if len(vars[key]) == 0 :
      html = html.replace('(*'+key+'*)', "")
    else :
      html = html.replace('(*'+key+'*)', vars[key])
  return html

# テンプレートファイルを指定する。(fileName はファイル名本体)
#   戻り値は HTMLテンプレート
def set_template(fileName, embed_vars=True) :
  result = ""
  html = "<html><head><title>Error</title></head><body>Error: Not found template file.</body></html>"
  try :
    with open(TEMPLATES + "/" + fileName) as f :
      html = f.read()
    if embed_vars :
      result = embed(html)
    else :
      result = html
  except :
    pass
  return result




## カスタマイズしたリクエストハンドラ
class HTApp(http.server.BaseHTTPRequestHandler) :

  # GET メソッドハンドラ
  def do_GET(self) :
    # クッキーを取得
    cookies = http.cookies.SimpleCookie()
    # リクエスト別の処理
    header = ['Content-Type', 'text/html']
    ext = os.path.splitext(self.path)[1]
    if ext == ".html" and self.path != '/' :
      # スタティックな HTML
      ppath = STATIC + self.path
      content = self.responseHtml(ppath)
    elif ext == ".jpg" or ext == ".png" or ext == ".gif" :
      # スタティックな画像
      ppath = STATIC + self.path
      content = self.responseImage(ppath)
      ext = self.__getImageType(ppath)
      header = ['Content-Type', 'image/' + ext]
    elif ext == ".css" :
      # スタティックな CSS
      ppath = STATIC + self.path
      header = ['Content-Type', 'text/css']
      content = self.responseHtml(ppath)
    elif ext == ".js" :
      # スタティックなスクリプト
      ppath = STATIC + self.path
      header = ['Content-Type', 'text/javascript']
      content = self.responseHtml(ppath)
    elif ext == ".svg" :
      # スタティックな SVG
      ppath = STATIC + self.path
      header = ['Content-Type', 'image/svg+xml svg']
      content = self.responseHtml(ppath)
    elif self.path == "/favicon.ico" :
      header = ['Content-Type', 'image/x-icon']
      content = self.responseImage("./html/favicon.ico")
    else :
      # 外部から来るGETパラメータを取得する。
      self.__getParams()
      # 動的な HTML (応答する内容を取得する)
      (type, content) = getContent(self.path, False)
      if type == "" :
        # エラーの場合
        self.send_error(int(content))
        return
      else :
        # 正常な場合
        header[0] = type
        header[1] = content
    # クライアントへ応答を返す。
    self.send_response(200)  # 常に 200 (OK) を返す。
    self.send_header(header[0], header[1])
    # クッキー
    for key in cookies :
      self.send_header("Set-Cookie", key + "=" + cookies[key])
    # ヘッダーを送る。
    self.end_headers()
    # コンテンツを送る。
    self.wfile.write(content)
    return

  # 外部から来るGETパラメータを取得する。
  def __getParams(self) :
    try :
      n = self.path.index('?')
    except :
      return
    data = self.path[n+1:len(self.path)]
    lparams = urllib.parse.parse_qs(data)
    params.clear()
    for key, arr in lparams.items() :
      params[key] = arr[0]
    return

  # POST メソッドハンドラ
  def do_POST(self) :
    # クッキーを取得
    cookies = http.cookies.SimpleCookie()
    # ヘッダーを定義
    header = ['Content-Type', 'text/html']
    # パラメータ入力先
    posted_file = self.rfile
    # 動的な HTML (応答する内容を取得する) のみ
    (type, content) = getContent(self.path, self.rfile)
    header[0] = type
    header[1] = content
    # クライアントへ応答を返す。
    self.send_response(200)  # 常に 200 (OK) を返す。
    self.send_header(header[0], header[1])
    # クッキー
    for key in cookies :
      self.send_header("Set-Cookie", key + "=" + cookies[key])
    # ヘッダーを送る。
    self.end_headers()
    # コンテンツを送る。
    self.wfile.write(content)
    return
 
  # テキスト(HTML, CSS, JAVASCRIPT, SVG)ファイルを応答として返す。
  def responseHtml(self, ppath) :
    if not os.path.isfile(ppath) :
      return b""  
    content = ""
    with open(ppath) as f :
      content = f.read()
    return content.encode('utf-8')
  
  # 画像ファイルを応答として返す。
  def responseImage(self, ppath) :
    if not os.path.isfile(ppath) :
      return b'0'
    content = None
    with open(ppath, "rb") as f :
      content = f.read()
    return content

  # パスから画像の種別を得る。
  def __getImageType(self, ppath) :
    ext = os.path.splitext(ppath)[1].lower()
    if ext == ".jpg" :
      ext = "jpeg"
    elif ext == '.png' :
      ext = 'png'
    else :
      ext = 'gif'
    return ext


    
# 開始
#conf = readConf()
#server = http.server.HTTPServer((SERVER_NAME, PORT), HTApp)
#print("START Server PORT=%d" % PORT)
#server.serve_forever()

