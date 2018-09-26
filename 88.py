import pickle
from collections import OrderedDict
from scipy import io
import numpy as np
f_in = "85.txt"
f_in2 = "84.txt"


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


# 辞書読み込み
with open(f_in, "rt") as data_file:
    dict_index = pickle.load(data_file)

# 行列読み込み
matrix_to_300 = io.loadmat(f_in2)["matrix_to_300"]
# io.loadmatで呼び出す際には、キーを用いて呼び出す。

# "England"とのコサイン類似度を算出
vec_England = matrix_to_300[dict_index["England"]]
distances = [cos_sim(vec_England, matrix_to_300[i]) for i in
            range(len(dict_index))]
# np.argsort()は並び替えた時のindexを返す
# sort()は並び替えた結果を返す。

# 上位10件を表示
index_sorted = np.argsort(distances)
keys = list(dict_index.keys())
for index in index_sorted[-2:-12:-1]:
    print("{}\t{}".format(keys[index], distances[index]))
