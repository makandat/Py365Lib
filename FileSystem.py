# FileSystem.py
# Version 1.00  2018-11-21
import os
import shutil
import glob
from pathlib import Path
import tempfile
import pwd
import grp

# テキストファイルを読んでその内容を返す。
def readAllText(file) :
  f = open(file)
  str = f.read()
  f.close()
  return str

# テキストをファイルに書く。
def writeAllText(file, str, append=False) :
  m = "w"
  if append == True :
    m = "a"
    with open(file, mode=m) as f :
      f.write(str)
  return

# ファイルを１行づつ読んで method で処理する。
def readAllLines(file, method) :
  with open(file) as f :
    for line in f:
      method(line.rstrip())
  return

# バイナリーファイルを読む。
def readBinary(file) :
  b = None
  with open(file, "rb") as f :
    b = f.read()
  return b

# バイナリーファイルを書く。
def writeBinary(file, data) :
  with open(file, mode='wb') as f :
    f.write(data)
  return

# INI ファイルを読む。
def readIni(file) :
  map = {}
  with open(file) as f :
    for s in f :
      if not ("=" in s) :
        continue
      kv = s.split('=')
      key = kv[0].strip()
      value = kv[1].strip()
      map[key] = value
  return map

# ファイルをコピーする。
def copy(src, dest) :
  shutil.copy(src, dest)
  return

# ファイルを移動する(名前の変更)
def move(src, dest) :
  shutil.move(src, dest)
  return

# ファイルやリンクを削除する。
def unlink(file) :
  os.unlink(file)
  return

# ファイルやディレクトリが存在するか調べる。
def exists(file) :
  return os.path.exists(file)

# ファイルが存在するか調べる。
def isFile(file) :
  return os.path.isfile(file)

# ディレクトリが存在するか調べる。
def isDirectory(dir) :
  return os.path.isdir(dir)

# リンクかどうか調べる。
def isLink(path) :
  return os.path.islink(path)

# ファイルやディレクトリの属性を得る。
def getAttr(path) :
  return os.stat(path).st_mode

# ファイルやディレクトリのオーナーを得る。
def getOwner(path) :
  uid = os.stat(path).st_uid
  name = pwd.getpwuid(uid).pw_name
  return name

# ファイルやディレクトリのグループを得る。
def getGroup(path) :
  gid = os.stat(path).st_gid
  name = grp.getgrgid(gid).gr_name
  return name

# カレントディレクトリを変更する。
def chdir(dir) :
  os.chdir(dir)
  return

# ディレクトリを作成する。
def mkdir(dir) :
  try :
    os.mkdir(dir)
  except :
    os.makedirs(dir)
  return

# ディレクトリを削除する。
def rmdir(dir) :
  try :
    os.rmdir(dir)
  except :
    shutil.rmtree(dir)
  return

# ファイル内の文字列を検索する。(行番号のリストを返す)
def grep(str, file) :
  result = []
  with open(file) as f :
    for i, line in enumerate(f) :
      if str in line :
        result.append(i)
  return result

# 指定したワイルドカードでディレクトリ内を検索する。
def listFiles(dir, wildcard="*") :
  list = glob.glob(dir + "/" + wildcard)
  result = []
  for item in list :
    if os.path.isfile(item) :
      result.append(item)
  return result

# ディレクトリ一覧を得る。
def listDirectories(dir) :
  list = os.listdir(dir)
  result = []
  for item in list :
    fpath = dir + "/" + item
    if os.path.isdir(fpath) :
      result.append(fpath)
  return result

# パス名の中でファイル名部分を返す。
def getFileName(path) :
  return os.path.basename(path)

# パス名の中でディレクトリ名部分を返す。
def getDirectoryName(path) :
  return os.path.dirname(path)

# パス名の中で拡張子部分を返す。
def getExtension(path) :
 p = os.path.splitext(path)
 if len(p) >= 2 :
   ext = p[1]
 else :
   ext = ""
 return ext

# 拡張子を変更する。(ext は新しい拡張子。先頭はドットであること)
def changeExt(path, ext) :
  p = os.path.splitext(path)
  return p[0] + ext

# 相対パスから絶対パスを得る。
def getAbsolutePath(path) :
  return os.path.abspath(path)

# 親のディレクトリを得る。
def getParentDirectory(path) :
  return Path(path).parent

# カレントディレクトリを得る。
def getCurrentDirectory() :
  return os.getcwd()

# 一時ファイル(パス名)を得る。
def getTempFile() :
  return tempfile.NamedTemporaryFile().name

