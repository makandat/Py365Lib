#!/usr/bin/python3
#   csv2json.py
#  TkApp Designer で作った CSV ファイルを JSON ファイルに変換する。
#   使用例  python3 csv2json.py tkapp101.csv
import os
from Common import *
from FileSystem import *

def quote(text) :
    return '"' + text + '"'

def chop(text) :
    return text[0:len(text)-1]

def csv2json(csvfile, jsonfile) :
    buff = "{"
    with open(csvfile) as f :
        line =f.readline()
        while line :
            line = chop(line)
            print(line)
            ss = line.split('\t')
            key = ss[0]
            value = ss[1]
            if key == "text" :
                buff += quote(key)
                buff += ":"
                buff += quote(value)
                buff += ","
            elif value != "" :
                buff += quote(key)
                buff += ":"
                if value[0] == "(" :
                    value = value.replace("(", "[")
                    value = value.replace(")", "]")
                    buff += value
                    buff += ","
                elif value[0] == "[" :
                    buff += value
                    buff += ","
                else :
                    try :
                        n = int(value)
                        buff += str(n)
                    except :
                        buff += quote(value)
                    buff += ","
            else :
                pass
            line = f.readline()
    n = len(buff)
    if buff[n-1] == "," :
        buff = buff[0:(n-1)]
    buff += "}\n"
    with open(jsonfile, "w") as fw :
        fw.write(buff)
    return
        

# コマンド引数の確認
if count_args() == 0 :
    print(ESC_FG_RED + "CSV ファイルを指定してください。")
    print(ESC_NORMAL)
    exit(9)

# CSV ファイル
csvfile = args()[0]
print("入力 " + csvfile)

# JSON ファイルの名前を決める。
jsonfile = os.path.splitext(csvfile)[0] + ".json"
print("出力 " + jsonfile)

# 変換して保存
csv2json(csvfile, jsonfile)

print("終わり。")
