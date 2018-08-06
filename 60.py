# kvs：Key-Value-Store
# https://qiita.com/uenohara/items/23eb6ee1259f8a927445
# LevelDBはGoogleがBigTableのアーキテクチャをベースにOSS化したKVS
# https://qiita.com/Morio/items/7538a939cc441367070d
# jsonは、データ形式の一つ。
import gzip
import json
import leveldb

fname = 'artist.json.gz'
fname_db = 'test_db'

# LevelDBオープン、なければ作成
db = leveldb.LevelDB(fname_db)

# gzファイル読み込み、パース
with gzip.open(fname, 'rt') as data_file:
    for line in data_file:
        data_json = json.loads(line)  # json.load()をすると、辞書型で読まれる

        # key=name+id、value=areaとしてDBへ追加
        key = data_json['name'] + '\t' + str(data_json['id'])
        value = data_json.get('area', '')  # getメソッドでキーから値を取得
        # getを使うと、キーがなくてもエラーがなく、['']だとエラー足出ない
        # get(key, x)としたら、keyが辞書にないときに、xを出力
        db.Put(key.encode(), value.encode())
        # dbはkeyとvalueどちらも、バイト列で指定する必要がある。


# 確認のため登録件数を表示
print('{}件登録しました。'.format(len(list(db.RangeIter(include_value=False)))))
# include_valud=Falseで、keyのみ取得できる
# RangeIterで、登録内容全件にアクセスできるイテレータが生成できる。
