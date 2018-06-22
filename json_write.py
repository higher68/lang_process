import gzip
import json
import re
fname = 'jawiki-country.json.gz'

def extract_UK():
    with gzip.open(fname, 'rt') as file:
        for line in file:
            data_json = json.loads(line)
            #JSON JavaScript 言語の表記法をベースにしたデータ形式
            #うーん。よくわからん。jsonの中身をlineで書いてるのが特に
            #print(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']
    raise ValueError('イギリス関連の記事が見つからない')
#print(extract_UK())
f = open('jsonkun.txt','w')
f.write(extract_UK())
f.close()
