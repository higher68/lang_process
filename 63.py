import gzip
import json
import re
import leveldb

fname = 'artist.json.gz'
fname_db = 'test_db'

# keyをnameとidに分解するための正規表現
pattern = re.compile(r'''
    ^
    (.*)    # name
    \t      # 区切り
    (\d+)   # id
    $       # 文末
    ''', re.VERBOSE + re.DOTALL)
# LevelDBオープン、ない時だけ作成
# try-excepr文
# try:
#   例外が発生するかもしれないが、実行したい処理
# except エラー名：
#   例外発生時の処理
try:
    db = leveldb.LevelDB(fname_db, error_if_exists=True)
    # error_if_exits = Trueで、データベースが存在する時はエラーになる
    # gzファイル読み込み、パース
    with gzip.open(fname, 'rt') as data_file:
        for line in data_file:
            data_json = json.loads(line)

            # name+idとtagsをDBへ追加
            key = data_json['name'] + '\t' + str(data_json['id'])
            valud = data_json.get('tags')       # tagsはないことがある
            if value in None:
                value = []
            db.Put(key.encode(), json.dumps(value).encode())
    # 確認のため登録件数表示
    print('{}件登録'.format(len(list(db.RangeIter(include_value=False)))))
except:
    db = leveldb.LevelDB(fname_db)
    print('既存のDBを使います。')

# 条件入力
