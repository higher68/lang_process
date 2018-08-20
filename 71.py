# stop-word：文章から特徴を抽出する際に対象外となる単語
# あまり意味をなさない単語
# 日本語の場合は、「は」、「を」などが相当する。
# ストップワードのリスト  http://xpo6.com/list-of-english-stop-words/ のCSV Formatより
# tuple:(, , )と書く。イミュータブル
# list:[]で書く。ミュータブル
stop_words = (
    'a,able,about,across,after,all,almost,also,am,among,an,and,any,are,'
    'as,at,be,because,been,but,by,can,cannot,could,dear,did,do,does,'
    'either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,'
    'him,his,how,however,i,if,in,into,is,it,its,just,least,let,like,'
    'likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,'
    'on,only,or,other,our,own,rather,said,say,says,she,should,since,so,'
    'some,than,that,the,their,them,then,there,these,they,this,tis,to,too,'
    'twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,'
    'will,with,would,yet,you,your').lower().split(',')


def is_stopped(str):
    '''文字がストップワードか判定
    大文字小文字は区別しない

    return
    ストップワード：True
    それ以外：False
    '''
    return str.lower() in stop_words


# assert 条件式, 条件式がFalseの場合に出力するメッセージ
# assert文を使うと例外が出るとエラーを返し、停止してくれる
# 正しく抽出されるテスト
assert is_stopped('a')  # リストの先頭
assert is_stopped('your')  # リストの末尾
assert is_stopped('neither')  # リストの中間
assert is_stopped('OWN')  # 大小文字の同一視
assert is_stopped('We')  # 大小文字の同一視
assert is_stopped('werE')  # 大小文字の同一視

# 誤抽出されない確認
assert not is_stopped('0')  # リストになし
assert not is_stopped('あ')  # リストになし
assert not is_stopped('youe')   # 後方不一致
assert not is_stopped('yo0r')   # 前方不一致
assert not is_stopped('hour')   # 中間不一致
assert not is_stopped(' ')   # 空白
assert not is_stopped('\n')   # 制御コード
assert not is_stopped('')   # 空文字
