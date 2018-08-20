# stopwordを除く
import codecs
import snowballstemmer  # 52本目を参照
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
