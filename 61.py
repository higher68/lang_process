import re  # 正規表現を使って探す
import leveldb

fname_db = 'test_db'

# keyをnameとidに分割するための正規表現
pattern = re.compile(r'''
    ^
    (.*?)
    \t
    (\d+)  # \dは数字 + は直前の表現の繰り返し
    $
    ''', re.VERBOSE + re.DOTALL)
# re.VERBOSEで、正規表現内にコメントをかける
# .を使うと、改行文字にもマッチする

# LevelDBをオープンする
db = leveldb.LevelDB(fname_db)

# 条件入力
clue = input('アーティスト名を入力してください--> ')
hit = False
# rangeiter()は、key_fromでイテレータの開始条件を指定できる
# leveldbのソートはよくわからん
# key_toで終了条件も指定可能
# keyはnameとidが合体した形になってる。
for key, value in db.RangeIter(key_from=(clue + '\t').encode()):
    # keyをnameとidに戻す
    match = pattern.match(key.decode())
    print(type(match))  # matchクラスに.group()が使えるんだなあ
    name = match.group(1)
    id = match.group(2)

    # アーティストが異なるものになったらbreak
    if name != clue:
        break

    # 活動場所のチェック、表示
    area = value.decode()
    if area != '':
        print('{}(id:{}の活動場所は{})'.format(name, id, area))
    else:
        print('{}(id:{}の活動場所は登録されていません)'.format(name, id))
    hit = True

# そもそもデータベースに登録されてなかったら
if not hit:
    print('{}は登録されていません'.format(clue))
