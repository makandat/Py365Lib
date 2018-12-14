#!/usr/bin/env python3
#  プログラムソース表示
import FileSystem, WebPage, Text

class ShowSource(WebPage.WebPage) :
  # コンストラクタ
  def __init__(self, template) :
    super().__init__(template)
    if 'path' in self.params :
      path = self.params['path'].value
      self.vars['message'] = path
      self.vars['filename'] = FileSystem.getFileName(path)
      self.show_src(path)
    else :
      self.vars['message'] = "ERROR: Parameter 'path' is not found."
      self.vars['filename'] = 'No path'
      self.vars['source'] = "Not found the file."

  # ソースファイルを読んで source に格納
  def show_src(self, path) :
    buff = FileSystem.readAllText(path)
    buff = Text.replace('&', '&amp;', buff)
    buff = Text.replace('<', '&lt;', buff)
    buff = Text.replace('>', '&gt;', buff)
    self.vars['source'] = buff


# メイン開始位置
wp = ShowSource('templates/show_source.html')
wp.echo()
