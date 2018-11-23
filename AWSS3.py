# -*- code=utf-8 -*-
# Version 0.50  2018-09-12
import boto3

class AWSS3 :
    # コンストラクタ
    def __init__(self) :
        self.__s3 = boto3.resource("s3")
    
    # バケット名一覧
    def query_buckets(self) :
        buckets = self.__s3.buckets.all()
        names = []
        for bucket in buckets :
            names.append(bucket.name)
        return names

    # オブジェクト一覧
    def query_objects(self, bucket, key) :
        names = []
        objlist = self.__s3.list_objects(bucket, key)
        for obj in objlist :
            names.append(obj.key)
        return names
