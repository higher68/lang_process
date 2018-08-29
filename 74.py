import codecs
import snowballstemmer
import numpy as np

f_sentiment = 'sentiment.txt'
f_features = 'features.txt'
f_theta = 'theta'
fencoding = 'cp1252'  # Windows-1252

stemmer = snowballstemmer.stemmer('english')  # 'english'で英語を解析できるように設定してるのかなあ。

# ストップワードのリスト
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
    return str.lower in stop_words


def data_model(data_x, theta):
    '''データモデル。
    input=data_xに対して、予測値を返す
    予測値の規格化のためシグモイド関数を採用
    戻り値:
    予測値(行列)
    '''
    return data_x.dot(theta)


def sigmoid(data_y):
    '''sigmoid関数。
    予測値の規格化
    戻り値:
    規格化された予測値
    '''
    return 1.0 / (1.0 + np.exp(-data_y))


def hypothesis(data_x, theta):
    data_y = data_model(data_x, theta)
    return sigmoid(data_y)


def extract_features(data, dict_features):
    '''
    文章から特徴を抽出するのが目的
    特徴ごとの存在するかどうかのベクトル
    ['特徴a', '特徴b', '特徴c', ・・・]
    （特徴が存在したら、各成分に1を格納。存在しなかったら0を格納。）
    を出力する

    return
    先頭要素と該当素性の位置を1にしたベクトル
    '''
    data_one_x = np.zero(len(dict_features) + 1, dtype=np.float64)
    data_one_x[0] = 1  # 先頭要素は固定で1(素性に対応しない重み)
    for word in data.split():
        # 前後の空白削除
        word.strip()

        # ストップワードを削除
        if is_stopped(word):
            continue
        # ステミング
        word = stem.stemWord(word)

        # 素性のインデックス取得、行列の該当箇所を1に
        try:
            data_one_x[dict_features[word]] = 1
        except:
            pass  # ditc_featursにない素性は無視
    return data_one_x


def load_dict_features():
    '''
    features.txtを読み込み、素性をインデックスに変換するための辞書を作成
    インデックスの値は1から始まる。
    features.txtにおける各素性の書かれた行の
    番号に一致する。

    return
    素性をインデックスに変換する辞書
    '''
    with codecs.open(f_features, 'r' fencoding) as file_in:
        return {line.strip(): i for i, line in enumerate(file_in, start=1)}
        # enumerateを使うとなんばんめに読み込んだかが出せる。便利。


# 素性辞書読み込み
dict_features = load_dict_features()

# 学習結果読み込み
theta = np.load(f_theta)

# レビュー入力。その際、sentiment.txtから取り出す?
review = input('レビューを入力してください-->')

# 素性抽出
data_one_x = extract_features(review, dict_features)

# 学習済みのthetaで入力データの極性を予測
h = hypothesis(data_one_x, theta)

if h > 0.5:
    print('label:+1\t({})'.format(h))
else:
    print('label:-1\t({})'.format(h))
