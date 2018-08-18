
from string import Template
import pymongo
from pymongo import MongoClient
import cgi
import cgitb
from html import escape


# 詳細なエラー情報をブラウザで表示
cgitb.enable()  # cgiプログラムの実行中に発生したエラー内容を
# ブラウザに表示
# cgi:command gateway interface
# webサーバと外部実行プログラムの間のインターフェース
# プログラムをhttpサーバで動かすためのルールと仕組み

max_view_count = 20  # 最大結果表示数

# HTML全体のテンプレート
# なんかよーわからんが、文字列の中の置換をしやすくしてくれるっぽい
# templateクラスは。
# htmlのタグは基本的に入れ子構造。xmlと似てるか？
# head：ファイル自身のヘッダ情報を示す部分
# body：ブラウザ上で実際に見える部分
# title:ファイル自身のタイトルを示す。ブラウザ上ではタブの部分に表示
# http-equiv:meta要素に指定すると、metaがプラグマ指示子となる
# プラグマ指示子：プラグマを指定するための名前
# 該当文書の処理方法、扱いを指定できる
# プラグマ：ユーザエージェントへの指示
# ユーザエージェント：利用者があるプロトコルに
# 基づいてデータを利用する際に用いるソフト・ハードウェア
# content-type：文字コード指定に使う
# text/html：ファイルの種類がhtmlファイルであることを示す
# htmlファイル：htmlのルールにしたがって書かれたテキストファイル
# html：ホームページのファイル書き方のルール
# ファイルのタイプがmimeタイプ(普通のテキスト、htmlファイルなど)
template_html = Template('''
<html>
    <head>
        <title>言語処理100本ノック2015 問題69</title>
        <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    </head>
    <body>
        <form method="GET" action="/cgi-bin/main.py">
            名前、別名:<input type="text" name="name" value="$clue_name" size = "20" /><br />
            タグ:<input type="text" name="tag" value="$clue_tag" value="$clue_tag" size="20" /><br />
            <input type="submit" value="検索"/>
        </form>
        $message
        $contents
    </body>
</html>
''')
# https://www.kanzaki.com/docs/html/htminfo31.html
# formaの中身に関する記述が上
# inputようそ：ユーザからの入力を受け入れるための手段を構成する。
# textタイプだと、短い文字列を入力するコントロールを提供　
# submitタイプは、送信指令をコントロールできる
# form method：送信するときの転送方法を指定する。
# 入力、送信フォームを作る時に使用
# getに指定すると、入力したフォーム内容のデータがuriにくっついて送信される
# action属性：データの送信先を指定する
# uri:uri`は名前または場所を識別する書き方のルール、要するにデータの送信先
# uri=寿司
# url(にぎり寿司)；；；場所を示す書き方のルール
# urn（チラシずし）；；；名前を示す書き方のルール

# 結果表示部分(template_htmlの$contents部分)のテンプレート
# <hr> horizontal rule, 水平な罫線を表す
# <hr />となっている場合、タグの後ろの閉じがいらない
# <br />改行を表す
template_result = Template('''
    <hr />
    ($index件目/全$total件)<br />
    [名前] $name<br />
    [別名] $aliases<br />
    [活動場所] $area<br />
    [タグ] $tags<br />
    [レーティング] $rating<br />
''')
# $の意味がよくわからん

# testdbのコレクションartistにアクセス
client = MongoClient()
db = client.testdb
collection = db.artist


# 条件を作成
# FieldStorageメソッドを用いるとk送られてきたデータを扱える
# そのメソッドで、名前を指定したら値が取得できる
form = cgi.FieldStorage()
clue = {}
clue_name = ''  # 名前の入力欄の内容
clue_tag = ''  # タグの入力欄の内容

if 'name' in form:
    clue_name = form['name'].value
    clue = {'$or': [{'name': clue_name}, {'aliases.name': clue_name}]}

if 'tag' in form:
    clue_tag = form['tag'].value
    if len(clue) > 0:
        clue = {'$and': [clue, {'tags.value': clue_tag}]}  #名前をタグと組み合わせる
    else:
        clue = {'tags.value': clue_tag}  # タグのみ

# 検索、ソーと
contents = ''  # 検索結果部分の出力内容
total = -1  # 結果件数、検索がまだなら、-1
if len(clue) > 0:

    results = collection.find(clue)
    results.sort('rating.count', pymongo.DESCENDING)
    # pytmongo.DESCENDINGで逆順にcollectionがソートされる
    total = results.count()

    # 結果を整形
    dict_template = {}
    # if a in bで、bの中にaが含まれているか調べられる
    for i, doc in enumerate(result[0:max_view_count], start=1):

        # 結果の初期値をセット
        dict_template['index'] = i
        dict_template['total'] = total
        dict_template['name'] = escape(doc['name'])
        # escapeは、文字列内の特殊文字を特殊文字として扱う&とか。

        if 'aliases' in doc:
            dict_template['aliases'] = \
            ','.join(escape(alias['name']) for alias in doc['aliases'])
        else:
            dict_template['aliases'] = '(データなし)'

        if 'area' in doc:
            dict_template['area'] = escape(doc['area'])
        else:
            dict_template['area'] = '(データなし)'

        if 'tags' in doc:
            dict_template['tags'] = \
            ','.join(escape(tag['value']) for tag in doc['tags'])
        else:
            dict_template['tags'] = '(データなし)'

        if 'rating' in doc:
            dict_template['rating'] = doc['rating']['count'])
        else:
            dict_template['rating'] = '(データなし)'

        contents += template_result.substitute(dict_template)

# HTML全体のテンプレート用辞書に内容をセット
dict_template ={}
dict_template['clue_name'] = escape(clue_name)
dict_template['clue_tag'] = escape(clue_tag)
dict_template['contens'] = contents

if total > max_view_count:
    dict_template['message'] = '結果が多いため先頭{}件を表示しています'.format(max_view_count)
elif total == -1:
    dict_template['message'] = '検索条件を入力してください'
elif total = 0:
    dict_template['message'] = '該当するアーティストは見つかりませんでした'
else:
    dict_template['message'] = ''

print(template_html.substitute(dict_template))
