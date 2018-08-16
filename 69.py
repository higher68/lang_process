
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



)
