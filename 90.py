import pickle
from collections import OrderedDict
import numpy as np
from scipy import io
import word2vec

f_in = "81.txt"
f_word2vec = "85_word2vec.txt"
f_dict_index = "85_dict"
f_matrix = "85_matrix"

# word2vecでベクトル化。出力までやってくれる
# 1行目に用語数と次元数が空白区切で出力
# 2行目以降1行1用語、各行に用語と対応する各次元の値300個が空白区切で出力
word2vec.word2vec(train=f_in, output=f_word2vec,
                  size=300, threads=4, binary=0)
# word2vecを用いた結果生成された行列をよみこむ。辞書も作成
with open(f_word2vec, 'rt') as data_file:
    vec_info = data_file.readline().split()  # 先頭行のみ読み込み
    size_dict = int(vec_info[0])
    vec_dim = int(vec_info[1])

    dict_index = OrderedDict()
    matrix = np.zeros([size_dict, vec_dim], dtype=np.float64)

    for i, line in enumerate(data_file):
        vec_value = line.strip().split()
        dict_index[vec_value[0]] = i  # 値をキー、インデックスがvalue
        matrix[i] = vec_value[1:]

# 結果の書き出し
io.savemat(f_matrix, {"matrix_300": matrix})
with open(f_dict_index, "wb") as data_file:
    pickle.dump(dict_index, data_file)
