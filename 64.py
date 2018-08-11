import json
import gzip
import pymongo  # pymongo-install done
from pymongo import MongoClient

fname = 'artist.json.gz'
unit_bulk = 10000  # バルクインサートする単位(件)
# バルクインサートをすると、insertしたドキュメントがリスト化される？
# MongoDBのデータベースtestdbにコレクションartistを作成
client = MongoClient()
db = client.testdb  # testdbというデータベースを作る
collection = db.artist  # artistというコレクションを作る

# gzファイル読み込み
with gzip.open(fname, 'rt') as data_file:

    # 1行ずつパースしてbufに詰め込む
    buf = []
    for i, line in enumerate(data_file, 1):
        # enumerate(対象, 開始するインデックス番号)
        data_json = json.loads(line)
        # lineの中身をjson形式から普通のにする?
        buf.append(data_json)

        # unit_bulk件溜まったらartistへバルクインサート
        if i % unit_bulk == 0:
            collection.insert_many(buf)
            buf = []
            print('{}件追加完了'.format(i))
    # 最後のunit_bulkに入らなかった半端文の追加
    if len(buf) > 0:
        collection.insert_many(buf)
        print('{}件追加完了'.format(i))


# インデックス作成
collection.create_index([('name', pymongo.ASCENDING)])
# collection.create_indexで、インデックスをデータに対して作れる?
collection.create_index([('aliases.name', pymongo.ASCENDING)])
collection.create_index([('tags.value', pymongo.ASCENDING)])
collection.create_index([('rating.value', pymongo.ASCENDING)])
# ascendig；昇順、descending：降順
