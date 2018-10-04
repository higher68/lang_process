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

with open(f_diec, "rt") as data_file:
    dict_index = pickle.load(data_file)
