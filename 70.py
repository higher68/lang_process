# 2値分類
import codecs
import random

fname_pos = "rt-polarity.pos"
fname_neg = "rt-polarity.neg"
# 上記2ファイルはutf-8でエンコードされていない。
# windows-1252らしい
fencoding = 'cp1252'  # windows-1252
fname_smt = "sentiment.txt"

result = []

# read positive and add +1
# codecs.open(指定した文字コードで読み込んでくれる)
# エンコードされたファイルを指定した文字コードで開く。
# append：要素1つを追加
# extend：リストを追加
with codecs.open(fname_pos, 'r', fencoding) as file_pos:
    result.extend(['+1 {}'.format(line.strip()) for line in file_pos])

# read negative and add -1
with codecs.open(fname_neg, 'r', fencoding) as file_neg:
    result.extend(['-1 {}'.format(line.strip()) for line in file_neg])

# リストの中身をランダムソート
random.shuffle(result)

with codecs.open(fname_smt, 'w', fencoding) as file_out:
    print(*result, sep='\n', file=file_out)

# count nega & posi
cnt_neg = 0
cnt_pos = 0
with codecs.open(fname_smt, 'r', fencoding) as file_in:
    for _ in file_in:
        # startswith()指定した文字列で始まるかどうか判定
        if _.startswith("-1"):
            cnt_neg += 1
        if _.startswith("+1"):
            cnt_pos += 1

print("negative sentence: {}".format(cnt_neg))
print("positive sentence: {}".format(cnt_pos))
