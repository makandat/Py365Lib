# coding:utf-8
# Version 1.20  2019-01-19 機能強化
#   参考 http://cgi.tutorial.codepoint.net/intro
import os, sys, io
import cgi
import locale
import http.cookies as Cookie
import urllib.parse
from syslog import syslog


VERSION = '1.20'

#
#  WebPage クラス
# ================
class WebPage :
  APPCONF = "AppConf.ini"
        
    # コンストラクタ
  def __init__(self, template="") :
    self.extension = os.path.splitext(template)[1].lower()  # テンプレートファイルの拡張子
    self.headers = ["Content-Type: text/html"] # HTTP ヘッダーのリスト
    self.vars =    {}  # HTML 埋め込み変数
    self.params =  {}  # HTTP パラメータ
    self.conf =    {}  # AppConf.ini の値
    self.cookies = {}  # Cookie の値
    self.html = ""     # HTML (.html, .svg, .xml, .xsl, .json, .txt)
    self.binbuff = bytes() # バイナリー値 (.jpg, .png, .gif, zip, gz, wav, mp3, ogg, ogv, mp4) のバッファ
    # stdin, stdout のコードを UTF-8 にする。デフォルトは ASCII になっているので文字化けする。
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    # HTML テンプレートを設定する。
    if template == "" :
      pass
    else :
      try :
        self.loadFile(template)
      except :
        pass
    # AppConf.ini を読む。
    self.readConf()
    # HTTP パラメータを得る。
    form = cgi.FieldStorage()
    for k in form.keys() :
      self.params[k] = form[k]
    # クッキーを得る。
    if "HTTP_COOKIE" in os.environ :
      cc = Cookie.SimpleCookie()
      cc.load(os.environ["HTTP_COOKIE"])
      for k, v in cc.items() :
        self.cookies[k] = v

  # コンテンツを送信する。
  def echo(self) :
    syslog(self.extension)
    if self.extension == ".html" :
      # クッキーをヘッダーに追加
      for k, v in self.cookies.items() :
        self.headers.append("Set-Cookie: " + k + "=" + str(v))
      # ヘッダーを送信
      self.header()
      # 埋め込み変数を処理
      for k, v in self.vars.items() :
        self.html = self.html.replace("(*" + k + "*)", str(v))
      # HTML を送信
      if self.html != "" :
        print(self.html)
      else :
       return
    elif self.extension == '.txt' :
      WebPage.sendText(self.html)
    elif self.extension == '.json' :
      WebPage.sendJson(self.html)
    elif self.extension == '.xml' :
      print("Content-Type: application/xml\n")
      print(self.html)
    elif self.extension == '.svg' :
      print("Content-Type: image/svg+xml\n")
      print(self.html)
    elif self.extension == '.jpg' :
      syslog(str(len(self.binbuff)))
      buff = b"Content-Type: image/jpeg\n\n" + self.binbuff
      sys.stdout.buffer.write(buff)
    elif self.extension == '.png' :
      buff = b"Content-Type: image/png\n\n" + self.binbuff
      sys.stdout.buffer.write(buff)
    elif self.extension == '.gif' :
      buff = b"Content-Type: image/gif\n\n" + self.binbuff
      sys.stdout.buffer.write(buff)
    elif self.extension == '.zip' :
      buff = b"Content-Type: application/zip\n\n" + self.binbuff
      sys.stdout.buffer.write(buff)
    elif self.extension == '.gz' :
      buff = b"Content-Type: application/x-compress\n\n" + self.binbuff
      sys.stdout.buffer.write(buff)
    elif self.extension == '.wav' :
      buff = b"Content-Type: audio/wav\n\n" + self.binbuff
      sys.stdout.buffer.write(buff)
    elif self.extension == '.mp3' :
      buff = b"Content-Type: audio/mp3\n\n" + self.binbuff
      sys.stdout.buffer.write(buff)
    elif self.extension == '.ogg' :
      buff = b"Content-Type: audio/ogg\n\n" + self.binbuff
      sys.stdout.buffer.write(buff)
    elif self.extension == '.ogv' :
      buff = b"Content-Type: video/ogv\n\n" + self.binbuff
      sys.stdout.buffer.write(buff)
    elif self.extension == '.mp4' :
      buff = b"Content-Type: video/wav\n\n" + self.binbuff
      sys.stdout.buffer.write(buff)
    else :
      pass
    return
             
  # HTTP ヘッダーを送信する。
  def header(self) :
    for s in self.headers :
      print(s)
    print()
    return

  # キャッシュコントロールヘッダ(Cahce-Control)を追加する。
  #   value の例:  max-age=seconds, no-cache, no-store
  def cacheControl(value) :
    self.headers.append('Cache-Control: ' + value)
    return

  # コンテンツの有効期限を追加する。
  #    date の例: Wed, 21 Oct 2015 07:28:00 GMT
  def cacheExpires(date) :
    self.headers.append('Expiresl: ' + date)
    return



  # クッキーを登録する。
  def cookie(self, key, value) :
    self.cookies[key] =value
    return

  # cookie() のシノニム  v1.1 で追加
  def setCookie(self, key, value) :
    self.cookie(key, value)
    return

  # クッキーの値を返す。キーが存在しない場合は '' を返す。v1.1 で追加
  def getCookie(self, key) :
    if key in self.cookies :
      return self.cookies[key].value
    else:
      return ''

  # パラメータが存在するかどうかを返す。v1.1 で追加
  def isParam(self, key) :
    return key in self.params

  # パラメータの値を返す。キーが存在しない場合は '' を返す。v1.1 で追加
  def getParam(self, key) :
    if self.isParam(key) :
      return self.params[key].value
    else :
      return ''

  # AppConf.ini を読む。
  def readConf(self) :
    self.conf = {}
    if not os.path.exists(WebPage.APPCONF) :
      return
    with open(WebPage.APPCONF) as f :
      for line in f :
        if line[0] =='#' or line[0] == '[' or len(line) == 0:
          continue
        kv = line.split('=')
        if len(kv) == 2 :
          key = kv[0].strip()
          value = kv[1].strip()
          self.conf[key] = value
    return

  # アップロードされたファイルを保存する。
  def saveFile(self, key, dir) :
    filename = os.path.basename(self.params[key].filename)
    with open(f"{dir}/{filename}", "wb") as f :
      f.write(self.params[key].file.read())
    return

  # リダイレクト
  def redirect(self, url, wait=1) :
    html = '''<html>
<head>
<meta charset="utf-8" />
<title>redirect</title>
<meta http-equiv="refresh" content="{1};{0}" />
</head>
<body>
<div style="margin-left:25%;margin-top:50px;">
<a href="{0}">ジャンプしないときはここをクリックしてください。Click here</a>
</div>
</body>
</html>
'''
    if type(url) is str :
      self.html = html.format(url, wait)
    else :
      self.html = html.format(url.value, wait)
    self.cookies = {}
    return

  # タグ作成
  @staticmethod
  def tag(name, str) :
    return "<" + name + ">" + str + "</" + name + ">"

  # テーブル行を作成
  @staticmethod
  def table_row(iter) :
    buff = "<tr>";
    for s in iter :
      buff += "<td>"
      buff += str(s)
      buff += "</td>"
    buff += "<tr>\n"
    return buff

  # HTML エスケープ文字を変換
  @staticmethod
  def escape(str) :
    return str.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

  # 画像を送信する。
  @staticmethod
  def sendImage(file) :
    ext = os.path.splitext(file)[1].lower()
    if ext == '.jpg' :
      type = b"jpeg"
    elif ext == '.png' :
      type = b'png'
    else :
      type = b'gif'
    with open(file, "rb") as f :
      b = f.read()
    buff = b"Content-Type: image/" + type + b"\n\n" + b
    #buff = b"Content-Type: image/png\n\n" + b
    sys.stdout.buffer.write(buff)
    return

  # JSON テキストを応答
  @staticmethod
  def sendJson(json) :
    print("Content-Type: application/json\n")
    print(json)
    return

  # プレーンテキストを応答
  @staticmethod
  def sendText(str) :
    print("Content-Type: text/plain\n")
    print(str)
    return

  # 拡張子の判別(バイナリーファイルかどうか)
  @staticmethod
  def isBinaryFile(file) :
    binexts = ['.jpg', '.png', '.gif', '.zip', '.gz', '.wav', '.mp3', '.ogg', '.mp4']
    b = False
    ext = os.path.splitext(file)[1].lower()
    for x in binexts :
      if ext == x :
        b = True
        break
    return b

  # ファイルをバッファに読み込む。
  def loadFile(self, filePath) :
    if WebPage.isBinaryFile(filePath) :
      with open(filePath, mode='rb') as f :
        self.binbuff = f.read()
    else :
      with open(filePath, mode='r', encoding='utf-8') as f :
        self.html = f.read()
    return
