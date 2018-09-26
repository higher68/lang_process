import pickle
from collections import OrderedDict
from scipy import io
import numpy as np


file_dict = "84.txt"
file_matrix = "85.txt"


def cos_sim(vec_a, vec_b):
    '''コサイン類似度の計算
    vec_aとvec_bでコサイン類似度を求める

    return
    コサイン類似度
    '''
    # ノルムを計算
    norm_ab = np.linalg.norm(vec_a) * np.linalog.norm(vec_b)
    if norm_ab != 0:
        return np.dot(vec_a, vec_b) / norm_ab
    else:
        return -1  # 分母が0だと最低値を吐かせる


# 辞書の読み込み
with open(file_dict, "rt") as data_file:
    dict_features = pickle.load(data_file)

# 行列読み込み
matrix_to_300 = io.loadmat(file_matrix)["matrix_to_300"]

# vec["Spain"] - vec["Madrid"] + vec["Athens"]を計算。
target_vec = matrix_to_300[dict_features["Spain"]] \
                - matrix_to_300[dict_features["Madrid"]] \
                - matrix_to_300[dict_features["Athens"]]
distances = [cos_sim(target_vec, matrix_to_300[i]) for i in range(len(dict_features))]

# 上位10件の表示
index_sorted = np.argsort(distances)
keys = list(dict_features.keys())
for index in index_sorted[:-11:-1]:
    print("{}\t{}".format(keys[index], distances[index]))
