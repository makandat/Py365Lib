#!/usr/bin/python3
# -*- coding=utf-8 -*-
#  テストプログラム FileSystem
import sys
from Py365Lib import Common, FileSystem as fsys

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
    Common.exec(["./fsysTest.sh", "1"])
    s = fsys.readAllText(FILE1)
    print(s)
    # writeAllText()
    FILE2 = "./test2.txt"
    FILE3 = "./test3.txt"
    fsys.writeAllText(FILE2, "-- writeAllText --\nABC 000\n")
    fsys.writeAllText(FILE3, "-- writeAllText(append) --\n", append=False)
    fsys.writeAllText(FILE3, "ABC 012\nLOL\n", append=True)
    Common.exec(["./fsysTest.sh", "2"])
# readAllLines(file, method)
elif testNo == 2 :
    FILE4 = "./test4.txt"
    Common.exec(["./fsysTest.sh", "3"])
    fsys.readAllLines(FILE4, method)
# readBinary(file), writeBinary(file, data), readIni(file)
elif testNo == 3 :
    # readBinary
    Common.exec(["./fsysTest.sh", "4"])
    data = fsys.readBinary("./binary1.bin")
    print(data)
    # writeBinary
    fsys.writeBinary("./binary2.bin", b'\x08\x09\x0a')
    Common.exec(["./fsysTest.sh", "5"])
    # readIni
    m = fsys.readIni("./AppConf.ini")
    print(m)
#  copy, move, unlink, exists
elif testNo == 4 :
    DEST = "./AppConf.ini.bak"
    try :
        fsys.unlink("config.ini")
        print("unlink config.ini")
    except FileNotFoundError :
        pass
    fsys.copy("./AppConf.ini", DEST)
    if fsys.exists(DEST) :
        print(DEST + " exists.")
    fsys.move(DEST, "./config.ini")
# isDirectory, isFile, isLink
elif testNo == 5 :
    assert fsys.isDirectory("/"), "testNo=5, subNo=1"
    assert fsys.isDirectory("./FileSystem.py") == False, "testNo=5, subNo=2"
    assert fsys.isFile("../FileSystem.py"), "testNo=5, subNo=3"
    assert fsys.isFile(".") == False, "testNo=5, subNo=4"
    assert fsys.isLink("./FileSystem.py") == False, "testNo=5, subNo=5"
    assert fsys.isLink("/usr/bin/lz"), "testNo=5, subNo=6"
    print("Test #5 OK")
# getAttr, getOwner, getGroup
elif testNo == 6 :
    a = fsys.getAttr("../FileSystem.py")
    print("%o" % a)
    print(fsys.getOwner("../FileSystem.py"))
    print(fsys.getGroup("../FileSystem.py"))
# chdir, mkdir, rmdir, pwd, getCurrentDirectory
elif testNo == 7 :
    cd = fsys.getCurrentDirectory()
    fsys.chdir("..")
    print(fsys.getCurrentDirectory())
    fsys.chdir(cd)
    print(fsys.getCurrentDirectory())
    fsys.mkdir("./xxx")
    if not fsys.isDirectory("./xxx") :
        print("mkdir error.")
        exit(9)
    fsys.rmdir("./xxx")
    if fsys.isDirectory("./xxx") :
        print("rmdir error.")
        exit(9)
    print("Test #7 OK")
else :
    print("不正なテスト番号です。")


