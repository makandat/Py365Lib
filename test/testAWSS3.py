#!/usr/bin/python3
# -*- coding=utf-8 -*-
#  AWSS3 クラスのテスト
import sys
from Py365Lib import AWSS3 as aws

# テスト番号取得
if len(sys.argv) == 1 :
    print("テスト番号を指定してください。")
    exit(9)
else :
    testNo = int(sys.argv[1])

# インスタンス化
s3 = aws.AWSS3()

if testNo == 1 :
    buckets = s3.query_buckets()
    print(buckets)
else :
    print("不正なテスト番号です。")
