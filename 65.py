##!!!!!!!!!!exercute 64.py and setup testdb!!!!!!!!!!!!!
##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11
import json
from pymongo import MongoClient  # mongodbへのクエリをだす
from bson.objectid import ObjectId

def support_ObjectId(obj):
    '''json.dumps()でObjectIdを処理するための関数
    ObjectIdはjsonエンコードできない型なので、文字列型に変換する

    戻り値：
    ObjectIdから変換した文字列
    '''
    if isinstance(obj, ObjectId):
        return str(obj)     # 文字列として扱う
    raise TypeError(repr(obj) + " is not JSON serializable")


# MongoDBのデータベースtestdbのコレクションartistにアクセス
client = MongoClient()  # mongoclientのインスタンス作成
db = client.testdb  # mongodb内のデータベースの一つ、testdbを呼び出している
collection = db.artist  # databese内にあるコレクション〜rdbでいうテーブル〜を呼び出す
# rdb：リレーショナルデータベース
# rdbは全てのデータをテーブルというデータ形式で表現
# https://employment.en-japan.com/engineerhub/entry/2017/11/22/110000
# 検索
# collectionはfindで検索可能
# collection.findはcursorオブジェクトを返す
for i, doc in enumerate(collection.find({'name': 'Queen'}), start=1):

    # 整形して表示
    print('{}件目の内容：\n{}'.format(i,
        json.dumps(
            doc, indent='\t', ensure_ascii=False,
            sort_keys=True, default=support_ObjectId
        )
    ))
# jsonのエンコーダー：json.dumps() 辞書をjson形式の文字列として出力
# 引数を指定して整形可能
# json.load()  jsonファイルを辞書として読み込む
