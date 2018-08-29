import codecs
import snowballstemmer
import numpy as np

# 重み：thetaのことなので、thetaの中の値でソート
f_features = 'features.txt'
f_theta = 'theta.txt'
fencoding = 'cp1252'  # Windows-1252

# 学習結果=theta＝重みの読み込み
theta = np.load(f_theta)

# 文字列表示のために特徴量を読み込み
with codecs.open(f_features, "r", fencoding) as file_in:
    features = list(file_in)

# 重みをソートascend
# numpy.argsort()は特定の行または列基準にソートしたいときに使える
# defaulは昇順
# inputは基準となる行or列のインデックスのリスト？

# 重みでソートした時の、インデックス番号の並びをリストにする
# thetaはもともと値のみが順番に書き込まれてる1次元配列なので、
# argsortにそのまま入れてよく、入れるとインデックス番号の配列が出てくる
index_sorted = np.argsort(theta)
