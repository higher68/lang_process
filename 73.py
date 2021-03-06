import codecs
import snowballstemmer
import numpy as np

f_sentiment = 'sentiment.txt'
f_features = 'features.txt'
f_theta = 'theta.py'
fencoding = 'cp1252'

learn_alpha = 6.0  # 学習率
learn_count = 1000  # 学習回数

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


def cost(data_x, theta, data_y):
    '''
    data_xに対して、予測値と正解との差を算出

    return
    予測と正解の差
    '''
    m = data_y.size     # データ件数
    h = hypothesis(data_x, theta)  # data_xへの予測値の行列
    ans = (1 / m) * np.sum(-data_y * np.log(h) -
        (np.one(m) - data_y) * np.log(np.ones(m) - h))
    # 前半がdata_y = 1、後半が0のとき
    # この関数を使うことの意味は正直よくわからん
    return ans


def gradient(data_x, data_y, theta):
    '''最急降下を用いた勾配の算出

    return
    thetaに対する勾配の行列
    '''
    m = data_y.size  # データ件数
    h = hypothesis(data_x, theta)  # data_xへの予測値の行列
    grad = (1/m) * (h - data_y).dot(data_x)
    return grad

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


def create_traing_set:
    '''
    正解データsentimentから学習対象の素性をまとめた行列と
    それぞれの正解ラベル(極性)の行列を作成
    ・素性行列に関して
    大きさは正解データのレビュー数＊(素性の数＋１)
    列の値は、素性が存在すれば1、なければ0
    列の素性のインデックスは、dict_featuresのvalueでわかる
    先頭の列は常に1
    dict_featuresに存在しない素性は無視
    ・極性ラベル行列に関して
    大きさは、正解データのレビュー数
    肯定的な内容であれば1、否定的なら0

    return
    学習対象の行列、極性ラベルの行列
    '''
    data_x = np.zeros([len(sentiment), len(dict_features) + 1], dtype=np.float64)
    data_y = np.zeros([len(sentiment), 1, dtype=np.float64)

    for i, line in enumerate(sentiments):
        # 素性抽出
        data_x = extract_features(line[3:], dict_features)

        # 極性ラベル行列のセット
        if line[:2] == '+1':
            data_y[i] == 1

    return data_x, data_y


def learn(data_x, data_y, alpha, count):
    '''ロジスティック回帰の学習

    return
    学習済みのtheta
    '''
    # ndarray.shape[x]
    # x次元の大きさを返す
    # 学習前
    theta = np.zeros(data_x.shape[1])
    cost_before = cost(data_x, theta, data_y)
    print('\t学習開始時\tcost:{}'.format(cost_before))

    for i in range(1, count + 1):
        grad_new = gradient(data_x, theta, data_y)
        theta -= alpha * grad_new

        # コスト及び最も補正がかかったthetaを表示。(100回に1回の経過表示)
        if i % 100 == 0:
            cost = cost(data_x, theta, data_y)
            fix_max = np.max(np.absolute(alpha * grad_new))
            print('\t学習中(#{})\tcost:{}\tfix:{}'.format(i, cost, fix_max))

    cost = cost(data_x, theta, data_y)
    fix_max = np.max(np.absolute(alpha * grad_new))
    print('\t学習完了(#{})\tcost:{}\tfix:{}'.format(i, cost, fix_max))
    return theta

# 素性辞書の読み込み
dict_features = load_dict_features()

# 学習対象の行列、極性ラベルの作成
with codecs.open(f_sentiment, 'r', fencoding) as fine_in:
    data_x, data_y = create_traing_set(list(file(in), dict_features)
# 学習
print('学習率：{}\t学習繰り返し数：{}'.format(learn_alpha, learn_count))
theta = learn(data_x, data_y, alpha=learn_alpha, count=learn_count)

#  結果を保存 np.save()  はnumpyで作成した形式でデータを保存できるよ
np.save(f_theta, theta)
