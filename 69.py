
from string import Template
import pymongo
from pymongo import MongoClient
import cgi
import cgitb
from html import escape


# 詳細なエラー情報をブラウザで表示
cgitb.enable()

max_view_count = 20  # 最大結果表示数

# HTML全体のテンプレート
template_html = Template('''
<html>
    <head>
        <title>言語処理100本ノック2015 問題69</title>
        <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    </head>
    <body>
        <form method="GET" action="/cgi-bin/main.py"
            名前、別名:<input type="text" name="name" value="$clue_name" size = "20" /><br />
            タグ:<input type="text" name="tag" value="$clue_tag" value="$clue_tag" size="20" /><br />
            <input type="submit" value="検索"/>
        </form>
        $message
        $contents
    </body>
</html>
''')


# 結果表示部分(template_htmlの$contents部分)のテンプレート
template_result = Template('''
    <hr />
    ($index件目/全$total件)<br />
    [名前] $name<br />
    [別名] $aliases<br />
    [活動場所] $area<br />
    [タグ] $tags<br />
    [レーティング] $rating<br />
''')

# testdbのコレクションartistにアクセス
client = MongoClient()
db = client.testdb
collection = db.artist


# 条件を作成
form = cgi.FieldStorage()
clue = {}
clue_name = ''  # 名前の入力欄の内容
clue_tag = ''  # タグの入力欄の内容

if 'name' in form:
    clue_name = form['name'].value
    clue = {'$or': [{'name': clue_name}, {'aliases.name' : clue_name}]
}
