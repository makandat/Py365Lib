#  Command/Index.py
#   Index.py v1.0.5  2021-09-22
import Common
from MySQL import MySQL
from WebPage import WebPage
import Handlers
#from MyError import Error
import CommandParser
import re

# Command CGI WebPage クラス
class Index(WebPage) :
  def __init__(self, template, conf=WebPage.APPCONF) :
    super().__init__(template, conf)
    # コマンド引数解析
    self._cc = None
    self._parser = None
    if self.getMethod() == 'GET' :
      if self.isParam('c') :  # コマンド
        cmd = self.getParam('c')
        if ' ' in cmd :
          cp = cmd.split(' ')
          self._cc = cp[0]
          if '"' in cmd :
            rp = re.compile(r'".*"')
            ms = rp.findall(cmd)
            self._parser = CommandParser.Parser(ms)
          else :
            self._parser = CommandParser.Parser(cp[1:])
        else :
          self._cc = cmd
      self.gets()
    elif self.getMethod() == 'POST' :
      self._cc = ""
      if self.isParam('c') :  # input[type="hidden"] で c を設定する。
        cmd = self.getParam('c')
        if ' ' in cmd :
          cp = self.getParam('c').split(' ')
          self._cc = cp[0]
          self._parser = CommandParser.Parser(cp[1:])
        else:
          self._cc = cmd
      self.posts()
    else :
      self.echo()  # コマンドが GET または POST でない場合はヘルプを表示
    return

  # コマンド名
  @property
  def cname(self) :
    return self._cc

  # c コマンドのパラメータ
  @property
  def parameters(self) :
    if self._parser is None:
      return []
    else:
      return self._parser.variables

  # c コマンドのオプション
  @property
  def options(self) :
    if self._parser is None:
      return {}
    else:
      return self._parser.options

  # GET メソッドのハンドラ
  def gets(self) :
    if self.cname == 'Hello' :
      Handlers.get_hello(self)
    elif self.cname == 'Echo':
      Handlers.get_echo(self)
    elif self.cname == 'index':  # カスタマイズ
      Handlers.get_index(self)
    elif self.cname == 'form':  # カスタマイズ
      Handlers.get_form(self)
    elif self.cname == 'getdata' :  # カスタマイズ
      Handlers.get_getdata(self)
    elif self.cname == 'show':  # カスタマイズ
      Handlers.get_show(self)
    elif self.cname == 'download':  # カスタマイズ
      Handlers.get_download(self)
    elif self.cname == 'object': # カスタマイズ
      Handlers.get_object(self)
    else :
      self.echo()
    return

  # POST メソッドのハンドラ
  def posts(self) :
    if self.cname == 'Echo' :
      Handlers.post_echo(self)
    else :
      Handlers.post_submit(self)  # Handlers のメソッドへ
    return

  # フォームデータを得る。(オーバーライドが必要)
  def getFormData(self, table, id) :
    return None
