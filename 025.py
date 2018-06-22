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
pattern = re.compile(r'''
    ^\{\{基礎情報.*?$
    (.*?)
    \}\}$
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)


#re.DOTALLは特殊文字 '.' を、改行を含むどんな文字にもマッチさせる
#*は直前の表現の0回以上の繰り返し。できるだけ長くマッチしようとする。
#*?は0回以上の繰り返し、+?は1回以上の繰り返し

contents = pattern.findall(extract_UK())
#print(len(contents))
print(contents)
pattern = re.compile(r'''
    ^\|
    (.+?)
    \s*
    =
    \s*
    (.+?)
    (?:
        (?=\n\|)
        | (?=\n$)
    )
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)
fields = pattern.findall(contents[0])
print('==================================')
print('==================================')
print('==================================')
print('==================================')
print('==================================')
print('==================================')
#(?=pattern)に関して。foo(?=bar)だと、fooのあとにbarが続くものにマッチ。
#(?=bar)fooだとbarが先にあるfooにマッチ。
#後読み、先読みはアンカー
#https://abicky.net/2010/05/30/135112/
result = {}
keys_test = []
for field in fields:
    result[field[0]] = field[1]
    keys_test.append(field[0])
print(keys_test)
print(result.items())
print('==================================')
print('==================================')
print('==================================')
print('==================================')
print('==================================')
print('==================================')
#sortedの第一引数は、sort対象
#.items：辞書オブジェクトに含まれる各要素について(キー, 値)のタプル型のオブジェクトを作成し、そのリストを取得するには
#https://www.pythonweb.jp/tutorial/dictionary/index8.html
#keyはリストの各要素に対して呼び出される関数を指定するパラメータです。
#lambda x: yはxを引数にして、yを出力する。
#.index：指定の値がリストの要素に含まれる場合に、それが含まれている位置(リスト内のインデックス)
#を出力する
#https://www.pythonweb.jp/tutorial/list/index10.html
for item in sorted(result.items(),
        key = lambda field: keys_test.index(field[0])):
    print(item)
#sortedの中身は、fieldをみて、keys_testの中身がfield[0]に一致。つまり、この場合は
#keys_testの中にfield[0]が含まれると、それを用いて名前順にresultの中身をリストにしたものを
#ソーとするというもの?
#resultをリスト化
#ソートを行った結果を順に出力。
#その際のソートは、リストの中の要素をみて
#その各要素が、keys_testの中でどのインデックスに位置するかを用いて
#ソートを行う。
