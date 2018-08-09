import json
import gzip
import pymongo
from pymongo import MongoClient

fname = 'artist.json.gz'
unit_bulk = 10000  # バルクインサートする単位(件)

# MongoDBのデータベースtestdbにコレクションartistを作成
client = MongoClient()
db = client.testdb
collection = db.artist

# gzファイル読み込み
with gzip.open(fname, 'rt') as data_file:

    # 1行ずつパースしてbufに詰め込む
    buf = []
    for i, line in enumerate(data_file, 1):
        data_json = json.loads(line)
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
