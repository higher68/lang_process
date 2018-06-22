#Wikipedia記事のJSONファイルを読み込み，
#「イギリス」に関する記事本文を表示せよ．問題21-29では，
#ここで抽出した記事本文に対して実行せよ．
import json
import gzip
with gzip.open('jawiki-country.json.gz', 'r') as f:
    for line in f:
        obj = json.loads(line)
        if obj['title'] == 'イギリス':
            print(obj['text'])
            break
#辞書形式でjson.loadは保存される。その際、キーを入れたら、参照できる。
#なおかつ、titleをキーとして入れた上で、textキーで２重参照できるっぽい
#
