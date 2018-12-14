#!/usr/bin/python3
# -*- coding=utf-8 -*-
#  テストプログラム FileSystem
import sys
from pprint import pprint
from Py365Lib import Common, FileSystem as fs

def method(s) :
    print(s)

# テスト番号取得
if Common.count_args() == 0 :
    Common.stop(9, "テスト番号を指定してください。") 
else :
    testNo = int(Common.args()[0])

# readAllText(file), writeAllText(file, str, append)
if testNo == 1 :
    # readAllText(file)
    FILE1 = "./test1.txt"
    Common.exec(["./fsTest.sh", "1"])
    s = fs.readAllText(FILE1)
    print(s)
    # writeAllText()
    FILE2 = "./test2.txt"
    FILE3 = "./test3.txt"
    fs.writeAllText(FILE2, "-- writeAllText --\nABC 000\n")
    fs.writeAllText(FILE3, "-- writeAllText(append) --\n", append=False)
    fs.writeAllText(FILE3, "ABC 012\nLOL\n", append=True)
    Common.exec(["./fsTest.sh", "2"])
# readAllLines(file, method)
elif testNo == 2 :
    FILE4 = "./test4.txt"
    Common.exec(["./fsTest.sh", "3"])
    fs.readAllLines(FILE4, method)
# readBinary(file), writeBinary(file, data), readIni(file)
elif testNo == 3 :
    # readBinary
    Common.exec(["./fsTest.sh", "4"])
    data = fs.readBinary("./binary1.bin")
    print(data)
    # writeBinary
    fs.writeBinary("./binary2.bin", b'\x08\x09\x0a')
    Common.exec(["./fsTest.sh", "5"])
    # readIni
    m = fs.readIni("./AppConf.ini")
    print(m)
#  copy, move, unlink, exists
elif testNo == 4 :
    DEST = "./AppConf.ini.bak"
    try :
        fs.unlink("config.ini")
        print("unlink config.ini")
    except FileNotFoundError :
        pass
    fs.copy("./AppConf.ini", DEST)
    if fs.exists(DEST) :
        print(DEST + " exists.")
    fs.move(DEST, "./config.ini")
# isDirectory, isFile, isLink
elif testNo == 5 :
    assert fs.isDirectory("/"), "testNo=5, subNo=1"
    assert fs.isDirectory("./FileSystem.py") == False, "testNo=5, subNo=2"
    assert fs.isFile("../FileSystem.py"), "testNo=5, subNo=3"
    assert fs.isFile(".") == False, "testNo=5, subNo=4"
    assert fs.isLink("./FileSystem.py") == False, "testNo=5, subNo=5"
    assert fs.isLink("/usr/bin/lz"), "testNo=5, subNo=6"
    print("Test #5 OK")
# getAttr, getOwner, getGroup
elif testNo == 6 :
    a = fs.getAttr("../FileSystem.py")
    print("%o" % a)
    print(fs.getOwner("../FileSystem.py"))
    print(fs.getGroup("../FileSystem.py"))
# chdir, mkdir, rmdir, pwd, getCurrentDirectory
elif testNo == 7 :
    cd = fs.getCurrentDirectory()
    fs.chdir("..")
    print(fs.getCurrentDirectory())
    fs.chdir(cd)
    print(fs.getCurrentDirectory())
    fs.mkdir("./xxx")
    if not fs.isDirectory("./xxx") :
        print("mkdir error.")
        exit(9)
    fs.rmdir("./xxx")
    if fs.isDirectory("./xxx") :
        print("rmdir error.")
        exit(9)
    print("Test #7 OK")
elif testNo == 8 :
    mslist = fs.readCsv('test8.csv')
    for m in mslist :
        pprint(m)
elif testNo == 9 :
    nlist = fs.grep("elif", "testFileSystem.py")
    for n in nlist :
        print(n)
else :
    print("不正なテスト番号です。")


