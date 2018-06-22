#記事中に含まれるセクション名とそのレベル
#（例えば"== セクション名 =="なら1）を表示せよ．
import gzip
import json
import re
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

#{m,n}はm回以上n回のカッコ内の繰り返し。
#={2,}だと2回以上=が繰り返されているとマッチ
#後方参照はここ参照。\numはnum番目の括弧で囲まれた文字列にマッチ。
#http://doc.okkez.net/static/1.8.7/doc/spec=2fregexp.html#backref
pattern = re.compile(r'''
    ^ #行頭文字
    (={2,}) #キャプチャ対象、２こ以上の'='
    \s* #空白文字。\tと同じ。
    (.+?) # キャプチャ対象、任意の文字が1文字以上、
    #非貪欲（以降の条件の巻き込み防止）
    \s* #*は0以上のくりかえし。できるだけ長くマッチ
    \1
    .*
    $
    ''', re.MULTILINE + re.VERBOSE)

result = pattern.findall(extract_UK())
#print(result)
for line in result:
    level = len(line[0]) - 1
    print('{indent}{sect}({level})'.format(
        indent='\t' * (level - 1), sect=line[1], level=level))
        #format関数を使うと任意の変数を引数にできる。
