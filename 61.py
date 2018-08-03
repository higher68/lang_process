import re
import LevelDB

fname_db = 'test_db'

# keyをnameとidに分割するための正規表現
pattern = re.compile(r'''
    ^
    (.*)    # name
    \t      # 区切り
    (\d+)   # id
    $
    ''', re.VERBOSE + re.DOTALL)

# LevelDBオープン
db = leveldb.LdvelDB(fname_db)

# 条件入力
clue = input('アーティスト名を入力してください--> ')
hit = False

for key, value in db.RangeIter(key_from=(clue + '\t').encode()):

    # keyをnameとidに戻す
    match = pattern.matcn(key.decode())
    name = match.group(1)
    id = match.group(2)

    # 異なるアーティストになったら終了
    if name != clue:
        break

    # 活動場所のチェック、表示
    area = value.decode()
    if area != '':
        print('{}(id:{})の活動場所：{}'.format(name, id, area))
    else:
        print('{}(id:{})の活動場所は登録されていません'.format(name, id))
    hit = True

if not hit:
    print('{}は登録されていません'.format(clue))
