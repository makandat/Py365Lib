#!/usr/bin/env python3
from Py365Lib import *

path = "/home/user/bin/rmcr.pl"

# ディレクトリ名を得る。
print(FileSystem.getDirectoryName(path))
# ファイル名を得る。
print(FileSystem.getFileName(path))
# 拡張子を得る。（先頭はドット）
print(FileSystem.getExtension(path))

# 現在の位置を得る。
print(FileSystem.getCurrentDirectory())
# 親のディレクトリを得る。
print(FileSystem.getParentDirectory("/home/user/bin"))
# 相対パスから絶対パスにを得る。
print(FileSystem.getAbsolutePath("../.."))

# 一時ファイル名を得る。
print(FileSystem.getTempFile())

