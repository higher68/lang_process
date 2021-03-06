# stopwordを除く
import codecs
import snowballstemmer  # 52本目を参照 語幹を抽出する。
from collections import Counter


f_sentiment = 'sentiment.txt'
f_features = 'features.txt'
fencoding = 'cp1252'    # Windows-1252

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


# stemming：単語の語幹を取り出す
# 素性（文章の特徴）抽出
stemmer = snowballstemmer.stemmer('english')  # 'english'で英語を解析できるように設定してるのかなあ。
# return stemmer object
word_counter = Counter()  # key=要素、 value=出現回数として要素の数を数えてくれる
i=0
with codecs.open(f_sentiment, 'r', fencoding) as file_in:
    for line in file_in:
        for word in line[3:].split():  # ラベルを削除
            # 余分な前後の空白削除
            word = word.strip()

            # ストップワード除去
            if is_stopped(word):
                continue

            # ステミング
            word = stemmer.stemWord(word)

            # '!'と'?'を除く1文字以下は除外
            if word != '!' and word != '?' and len(word) <= 1:
                continue

            # 候補に追加 counter object はupdateで追加するのか
            word_counter.update([word])
            print(word_counter.items())
            i+=1
            if i == 90:exit()
# 出現数が6以上のものを採用
# items()でキーとvalueのペアのタプタプルのリストを取得できる
features = [word for word, count in word_counter.items() if count >= 6]

# 書き出し
with codecs.open(f_features, 'w', fencoding) as f_out:
    print(*features, sep='\n', file=f_out)
