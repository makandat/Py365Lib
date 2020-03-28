#!/usr/bin/python3
# -*- coding=utf-8 -*-
#  テストプログラム(2) FileSystem
import sys
from pprint import pprint
from Py365Lib import Common, FileSystem as fs

def method(s) :
    print(s)

# テスト番号取得
if Common.count_args() == 0 :
    Common.stop(9, "テスト番号を指定してください。") 
else :
    testNo = int(Common.args(0))

# getHomeDirectory, getThisDirectory
if testNo == 1 :
  dir = fs.getHomeDirectory()
  print(dir)
  dir = fs.getThisDirectory('/home/user/workspace/python3')
  print(dir)
elif testNo == 2 :
  # listFiles
  files = fs.listFiles('/home/user/Pictures/Pixiv/こたつ')
  files.sort()
  pprint(files)
elif testNo == 3 :
  # listDirectories
  dirs = fs.listDirectories('/home/user')
  dirs2 = sorted(dirs)
  #pprint(dirs2)
  buff = "<ol>\n"
  for d in dirs2 :
    buff += "<li>" + d + "</li>\n"
  buff += "</ol>\n"
  print(buff)
elif testNo == 4 :
  # exists, isFile, isDirectory 日本語ファイルとフォルダ
  assert fs.exists('/home/user/ダウンロード') == True, "testNo. #4, subTest #1"
  assert fs.exists('/home/user/ダウンロー') == False, "testNo. #4, subTest #2"
  assert fs.isFile('/home/user/workspace/python3/Py365Lib/test/テスト.txt') == True, "testNo. #4, subTest #3"
  assert fs.isFile("/home/user/workspace/python3/Py365Lib/test/test (1).txt") == True, "testNo. #4, subTest #4"
  assert fs.isFile("/home/user/workspace/python3/Py365Lib/test/テスト (1).txt") == True, "testNo. #4, subTest #5"
  assert fs.isFile('/home/user/ミュージック') == False, "testNo. #4, subTest #6"
  assert fs.isDirectory('/home/user/ミュージック') == True, "testNo. #4, subTest #7"
  assert fs.isDirectory("'/home/user/workspace/python3/Py365Lib/test/テスト (1).txt'") == False, "testNo. #4, subTest #8"
  print("testNo #4 OK")
elif testNo == 5 :
  # listFilesRecursively
  files = fs.listFilesRecursively("/home/user/workspace/flask", asstr=True)
  for f in files :
    print(f)
elif testNo == 6 :
  # listFiles2  (os.listdir版)
  print("listFiles2  (os.listdir版)")
  files = fs.listFiles2("F:/Pictures/MANGA/Book01/PONPON/ぼいトレ！")
  for f in files :
    print(f)
  print('Done.')
  pass
elif testNo == 7 :
  pass
elif testNo == 8 :
  pass
elif testNo == 9 :
  pass
else :
    print("不正なテスト番号です。")


