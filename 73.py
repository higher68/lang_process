import codecs
import snowballstemmer
import numpy as np

f_sentiment = 'sentiment.txt'
f_features = 'features.txt'
f_theta = 'theta.py'
fencoding = 'cp1252'

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
