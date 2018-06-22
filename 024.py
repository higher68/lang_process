#24. ファイル参照の抽出
#記事から参照されているメディアファイルをすべて抜き出せ．
import gzip
import re
import json
fname = 'jawiki-country.json.gz'

def extract_UK():
    with gzip.open(fname, 'rt') as file:
    #rtにすると、テキストモードで読める。⇨strクラス
        for line in file:
            data_json = json.loads(line)
            #JSON JavaScript 言語の表記法をベースにしたデータ形式
            #うーん。よくわからん。jsonの中身をlineで書いてるのが特に
            #print(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']
    raise ValueError('イギリス関連の記事が見つからない')
#.は任意の一文字
#+直前の表現の1回以上の繰り返し
#?直前正規表現の0または1回の繰り返し。
#.+・・・任意の数の文字?・・・?をつけたら、任意の数の文字が一回現れたら
#キャプチャ停止。
#re.VERBOSEは、正規表現の途中にコメントを入れるために指定
pattern = re.compile(r'''
    (?:File|ファイル)
    :
    (.+?)
    \|
    ''', re.VERBOSE)

result = pattern.findall(extract_UK())

for line in result:
    print(line)

#print(extract_UK())
