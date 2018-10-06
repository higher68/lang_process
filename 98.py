# データ分類の手法
# 1：classification(クラス分類)・・・事前にグループ定義
# 2：clustering・・・事前に定義しない。
# 階層型クラスタリング・・・最も似ているものから段階的にまとめていく方法
# デンドログラム・・樹形図

import pickle
from collections import OrderedDict
from scipy import io
import numpy as np

from scipy.cluster.hierarchy import ward, dendrogram
from matplotlib import pyplot as plt

f_dict = "96_dict_index"
f_matrix = "96_matrix_300"
# 辞書読み込み
with open(f_dict, "rb") as data_file:
    dict_index = pickle.load(data_file)


# 読み込み
matrix_300 = io.loadmat(f_matrix)["matrix_300"]

# Ward法クラスタリング
# 結果は、[束ねたクラスターインデックス1, 束ねたクラスターインデックス2,  クラスター内所属データの距離の和, 束ねたクラスター内のデータ数]
ward = ward(matrix_300)
print(ward)

# デンドログラム表示
dendrogram(ward, labels=list(dict_index.keys()), leaf_font_size=8)
plt.show()
