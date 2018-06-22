#記事中でカテゴリ名を宣言している行を抽出せよ．
#
import json
import gzip
import re

fname = 'jawiki-country.json.gz'
with gzip.open(fname, 'r') as file:
    for line in file:
        data = json.loads(line)
        if data['title'] == 'イギリス':
            x = data['text']
            break
##rを最初につけると、バックスラッシュがそのままバックスラッシュ文字
#として使える
#r"文字列"でrawstringになる
pattern = re.compile(r'''
^ #行頭
( #キャプチャ対象のグループ化開始
.* #任意の0文字以上
\[\[Category:
.* #任意の0文字以上
\]\]
.* #任意の0文字以上
)  #グループ終了
$ #行末
''', re.MULTILINE + re.VERBOSE)

# MULTILINE, M ^ や $ に作用して、複数行にマッチング
#re.VERBOSEは、正規表現の途中にコメントを入れるために指定

result = pattern.findall(x)

for line in result:
    print(line)
