#正規表現のコンパイル=同じパターンで検索する時に、毎回
#パターンを指定することないように、検索式を作る
#https://qiita.com/wanwanland/items/ce272419dde2f95cdabc

import gzip
import json
import re
fname = 'jawiki-country.json.gz'


def extract_UK():
    ##イギリスに関する記事本文取得

    ##戻り値 イギリスの記事本文
    ##
    with gzip.open(fname, 'rt') as file:
        for line in file:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']

    raise ValueError('イギリスの記事が見つからない')
    #特定の例外を発生させる。まあ、要するに例外処理か
#正規表現のコンパイル
#正規表現内で、^文章$とすると、文章のある行にだけ合致
#.*はそこ以降の文字はなんでもいいということ。ここでは、最初の文字はなんでもということ
#で\[\[Category:で、[[Category:ってなってる部分
#パターン内でマッチする⇨文字列が記録される
#さらに記録された文字列をパターン内で参照できる。
#http://www.perlplus.jp/regular/ref/index5.html
#.はなんでもいい1文字
#*直前の文字がないか、連続する場合。⇨.*は適当な文字の連続
#()グループ化()で囲まれた文字列を一つとして扱える。
#非貪欲マッチ：できるだけ少ない文字数にマッチ
#(?:...)グループによって一度マッチしたら、二度とマッチされない
#https://www.javadrive.jp/regex/ref/index3.html
#?直前の文字が全くないか、一つだけある。
#(x)は()ないのパターンにマッチし、キャプチャする。キャプチャしたものは
#(?:x)xにマッチするが、キャプチャはしない
#後から参照できる
#http://kyu-mu.net/coffeescript/regexp/

pattern = re.compile(r'''
    ^   #行頭
    .*  #任意の文字0文字以上
    \[\[Category:
    (    #キャプチャ対処のグループ開始
    .*?  #任意の0文字以上、非貪欲マッチ（貪欲にすると後半の'|'で始まる装飾を巻き込んでしまう）
    )    #グループ終了
    (?:  #キャプチャ対象外のグループ開始
    \|.* #に続く0文字以上
    )?   # グループ終了、0か1回の出現
    \]\]
    .*   #任意の0文字以上
    $  #行末
    ''', re.MULTILINE + re.VERBOSE)
    # MULTILINE, M ^ や $ に作用して、複数行にマッチング
    #re.VERBOSEは、正規表現の途中にコメントを入れるために指定

print(extract_UK())
result = pattern.findall(extract_UK())
##findall()出現するパターン全てにマッチ
for line in result:
    print(line)
