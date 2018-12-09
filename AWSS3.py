# -*- code=utf-8 -*-
# Version 1.00  2018-12-09
import boto3

class AWSS3 :
    # コンストラクタ
    def __init__(self) :
        self.__s3 = boto3.resource("s3")
        self.buckets = list(self.__s3.buckets.all())
        self.objlist = {}
        return
    
    # バケット内のフォルダキー一覧
    def query_folders(self, bucketName, level, callback) :
        bucket = self.__s3.Bucket(bucketName)
        if bucketName in self.objlist.keys() :      
            self.objlist[bucketName] = bucket.objects.all()
        for obj in objlisti[bucketName] :
            if level < 0 and obj.key.endswith('/'):
                callback(obj.key)
            elif obj.key.endswith('/') and obj.key.count('/') == (level + 1):
                callback(obj.key)
            else :
                pass
        return

    # バケット内のファイルキー一覧
    def query_files(self, bucketName, key, callback) :
        bucket = self.__s3.Bucket(bucketName)
        if not bucketName in self.objlist.keys() :
            self.objlist[bucketName] = bucket.objects.all()
        for obj in objlist[bucketName] :
            if not obj.key.endswith('/') and obj.key.startswith(key) :
                callback(obj.key)
            else :
                pass
        return

    # キーが存在するか
    def exists(self, bucketName, key) :
        rc = False
        bucket = self.__s3.Bucket(bucketName)
        if not bucketName in self.objlist.keys() :
            self.objlist[bucketName] = bucket.objects.all()
        for obj in self.objlist[bucketName] :
            if obj.key == key :
                rc = True
                break
        return rc

    # ファイルを送信する。(クラウドに格納する)
    def put_file(self, bucketName, key, fileName) :
        bucket = self.__s3.Bucket(bucketName)
        bucket.upload_file(fileName, key)
        if bucketName in self.objlist :
            self.objlist[bucketName].append(key)
        return

    # ファイルを受信する。(クラウドから取得する)
    def get_file(self, bucketName, key, fileName) :
        bucket = self.__s3.Bucket(bucketName)
        bucket.download_file(key, fileName, None, None, None)
        return

    # フォルダキーを作成する。
    def make_folder(self, bucketName, key) :
        bucket = self.__s3.Bucket(bucketName)
        if not key.endswith('/') :
            key = key + "/"
        bucket.put_object(Key=key)
        if bucketName in self.objlist :
            self.objlist[bucketName].append(key)
        return

    # フォルダキー('/'で終わる)またはファイルを削除する。
    def remove_object(self, bucketName, key) :
        bucket = self.__s3.Bucket(bucketName)
        bucket.delete_objects(Delete={'Objects':[{'Key':key}]})
        if bucketName in self.objlist :
            del self.objlist[bucketName][key]
        return
    
