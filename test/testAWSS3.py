#!/usr/bin/python3
# -*- coding=utf-8 -*-
#  AWSS3 クラスのテスト
import sys
from pprint import pprint
from Py365Lib import AWSS3 as aws


def cb_keys(key) :
    print(key)
    return
    
# テスト番号取得
if len(sys.argv) == 1 :
    print("テスト番号を指定してください。")
    exit(9)
else :
    testNo = int(sys.argv[1])

# インスタンス化
s3 = aws.AWSS3()

if testNo == 1 :
    for bucket in s3.buckets :
        print(bucket.name)
elif testNo == 2 :
    s3.query_folders(s3.buckets[2].name, 1, cb_keys)
elif testNo == 3 :
    s3.query_files(s3.buckets[2].name, "images/akagi/", cb_keys)
elif testNo == 4 :
    print(s3.exists("small10be", "temp/disk.cgi"))
    print(s3.exists("small10be", "temp/1000.txt"))
elif testNo == 5:
    s3.put_file("small10be", "temp/testAWSS3.py", "testAWSS3.py")
elif testNo == 6:
    s3.get_file("small10be", "temp/200000.txt", "/home/user/temp/200000.txt")
elif testNo == 7:
    s3.make_folder("small10be", "folder/")
elif testNo == 8:
    s3.remove_object("small10be", "folder/")
else :
    print("不正なテスト番号です。")
