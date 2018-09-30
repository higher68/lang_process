import pickle
from collections import OrderedDict
from scipy import io
import numpy as np

f_dict = "84_dict_index"
f_matrix = "85_matrix_300"
f_in = "91_family.txt"
f_out = "92_family_out.txt"


def cos_sim(vec_a, vec_b):
    '''コサイン類似度の計算
    ベクトルvec_a、vec_bのコサイン類似度を求める

    戻り値：
    コサイン類似度
    '''
    norm_ab = np.linalg.norm(vec_a) * np.linalg.norm(vec_b)
    if norm_ab != 0:
        return np.dot(vec_a, vec_b) / norm_ab
    else:
        # ベクトルのノルムが0だと似ているかどうかの判断すらできないので最低値
        return -1


with open(f_dict, "rb") as data_file:
    dict_index = pickle.load(data_file)
keys = list(dict_index.keys())

matrix = io.loadmat(f_matrix)["matrix_300"]

with open(f_in, "rt") as data_file, \
     open(f_out, "wt") as out_file:

    for line in data_file:
        cols = line.split()

        try:
            vec = matrix[dict_index[cols[1]]] - \
                  matrix[dict_index[cols[0]]] + \
                  matrix[dict_index[cols[2]]]
            # コサイン類似度の一番高い単語を抽出
            dist_max = -1
            index_max = 0
            max_word = ""
            for i in range(len(dict_index)):
                dist = cos_sim(vec, matrix[i])
                if dist > dist_max:
                    dist_max = dist
                    index_max = i
            max_word = keys[i]

        except KeyError:
            # 単語がないときは0文字をコサイン類似度-1で出力
            result = ""
            dist_max = -1
        # ファイル出力
        print("{} {} {}".format(line.strip(), max_word, dist_max),
              file=out_file)
        # 標準出力
        print("{} {} {}".format(line.strip(), max_word, dist_max))
