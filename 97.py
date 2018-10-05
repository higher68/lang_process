# データ分類の手法
# 1：classification(クラス分類)・・・事前にグループ定義
# 2：clustering・・・事前に定義しない。
import pickle
from collections import OrderedDict
from scipy import io
import numpy as np
from sklearn.cluster import KMeans

f_dict = "96_dict_index"
f_matrix = "96_matrix_300"

with open(f_dict, "rt") as data_file:
    dict_index = pickle.load(data_file)


# 行列読み込み
matrix_300 = io.loadmat(f_matrix)["matrix_300"]

# KMeansクラスタリング
predicts = KMeans(n_clusters=5).fit_predict(matrix_300)
# predictsには、各行に対する分類番号(クラスター番号)が格納される
# (国,分類番号)のリスト作成
result = zip(dict_index.keys(), predicts)
# predictsは行番号にしたがって、分類番号が格納されている。
# なので、keysとzipで合体させてリストにする
for line in sorted(result, keys=lambda x: x[1]):
    print("{}\t{}".format(line[1], line[0]))
