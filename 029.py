import gzip
import json
import re
import urllib.parse, urllib.request
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

def remove_markup(target):
    '''マークアップの除去
    MediaWikiマークアップの可能な限りの除去

    引数：
    target -- 対象の文字列
    戻り値：マークアップを除去した文字列
    '''

    #print(0,target)
    #強調マークアップの削除
    pattern = re.compile(r'''
        (\'{2,5}) #2~5個の' # 2〜5個の'（マークアップの開始）
        (.*?) # 任意の1文字以上（対象の文字列）
        (\1)  # 1番目のキャプチャと同じ（マークアップの終了）、1番目でマッチしたものと同じものにマッチ
        ''', re.MULTILINE + re.VERBOSE)
    target = pattern.sub(r'\2', target)
    #rを前方に置いた文字列では、バックスラッシュを特別扱いしないアレ
    #print(1,target)
    #内部リンク、ファイルの除去
    pattern = re.compile(r'''
        \[\[    ##マークアップの開始
        (?:     #キャプチャ対象外
            [^|]*?   # '|'以外の文字が0文字以上、非貪欲
                #[]は文字クラス指定。[]内のいずれかの1文字にマッチ
                #上で先頭が^なら、指定した文字以外にマッチ。
            \|  # '|'
        )*?       # グループ終了、このグループが0か1出現
        ([^|]*?)  # キャプチャ対象、'|'以外が0文字以上、非貪欲（表示対象の文字列）
        \]\]
        ''', re.MULTILINE + re.VERBOSE)
    target = pattern.sub(r'\1', target)
    #print(2,target)
    #Template:langの除去
    pattern = re.compile(r'''
        \{\{lang  #'{{lang' (マークアップの開始)
        (?:
            [^|]*?
            \|
        )*?
        ([^|]*?) #*?直前の表現の0回以上の繰り返し。
        \}\}
        ''', re.MULTILINE + re.VERBOSE)
    #print(pattern.findall(target),r'\1')
    #単純に''とやると、{{lang|~}}全体が置換される。
    #つまり、正規表現
    #キャプチャとマッチは違うか。
    #subはパターンにあう部分をサーチし、そこの部分をreplaceで置き換えるらしい。
    #今回だと、patterをサーチして、そこをマッチの1つめで置き換え
    target = pattern.sub(r'\1', target)
    #print(3,target)
    #外部リンクの除去 [http://xxx], [http://xxx xxx]
    pattern = re.compile(r'''
        \[http:\/\/ #マークアップの開始
        (?:
            [^\s]*?
            \s
        )?
        ([^]]*?)  #*?直前の表現の0回以上の繰り返し
        \]
        ''', re.MULTILINE + re.VERBOSE)
    target = pattern.sub(r'\1', target)
    #sub関数の使い方？patternの正規表現で表される文字列をマッチ
    #マッチした文字列に関して、\1だったら1個目のマッチで置換
    #targetに関して、
    #print(4,target)

    #<br>, <ref>の除去
    pattern = re.compile(r'''
        <
        \/?
        [br|ref]
        [^>]*?
        >
        ''', re.MULTILINE + re.VERBOSE)

    target = pattern.sub('', target)
    #print(5,target)

    return target

    ##正規表現マッチしたところを指定した文字に変える。(target内)

#基礎情報抽出条件のコンパイル
pattern = re.compile(r'''
    ^\{\{基礎情報.*?$
    (.*?)
    \}\}$
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)


#re.DOTALLは特殊文字 '.' を、改行を含むどんな文字にもマッチさせる
#*は直前の表現の0回以上の繰り返し。できるだけ長くマッチしようとする。
#*?は0回以上の繰り返し、+?は1回以上の繰り返し

#基礎情報テンプレートの抽出
contents = pattern.findall(extract_UK())
#print(len(contents))
#print(contents)
#抽出結果kらのフィールド名と値の抽出条件コンパイル
pattern = re.compile(r'''
    ^\|
    (.+?)
    \s*
    =
    \s
    (.+?)
    (?:
        (?=\n\|)
        | (?=\n$)
    )
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

fields = pattern.findall(contents[0])

#辞書にセット
result = {}
for field in fields:
    result[field[0]] = remove_markup(field[1])

#国旗画像の値を取得
fname_flag = result['国旗画像']
#URLエンコード・・・URLでは使えない文字を変換する(encode)http://wa3.i-3-i.info/word13354.html

#リクエスト生成
url = 'http://mediawiki.org/w/api.php?' \
    + 'action=query' \
    + '&titles=File:' + urllib.parse.quote(fname_flag) \
    + '&format=json' \
    + '&prop=imageinfo' \
    + '&iiprop=url'
#urllib.parse.quoteはURLエンコードしてくれる関数っぽい

#MediaWikiのサービスへリクエスト送信
request = urllib.request.Request(url,
    headers={'User-Agent': 'NLP100_Python(@segavvy)'})
connection = urllib.request.urlopen(request)
#url を開きます。 url は文字列でも Request オブジェクトでも
#かまいません
#HTTP メッセージは、サーバーとクライアントがデータを交換する手段です。
#クライアントが送信してサーバーにアクションを起こさせるリクエストと、
#サーバーの回答であるレスポンスの、2 種類のメッセージがあります。
#Request オブジェクトを作成し、urlopen に渡すことでリクエストが送信される。


#jsonとして受信
data = json.loads(connection.read().decode())
#connctionの任意の数の文字を表示し、utfで表示？
#レスポンスをjsonで受信できるらしい。よくわからんが。

#URL取り出し
url = data['query']['pages'].popitem()[1]['imageinfo'][0]['url']
print(url)
