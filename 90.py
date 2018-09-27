import pickle
from collections import OrderedDict
import numpy as np
from scipy import io
import word2vec

f_in = "81.txt"
f_word2vec = "vectors.txt"
f_dict_index = "84.txt"
f_matrix = "85.txt"

# word2vecでベクトル化。出力までやってくれる
word2vec.word2vec(train=f_in, output=f_word2vec,
                  size=300, threads=4, binary=0)
#
with open(f_word2vec, 'rt') as data_file:
    vec_info = data_file.readline().split()  # 先頭行のみ読み込み
    size_dict = int(vec_info[0])
    vec_dim = int(vec_info[1])

    dict_index = OrderedDict()
    matrix = np.zeros([size_dict, vec_dim], dtype=np.float64)

    for i, line in enumerate(data_file):
        vec_value = line.strip().split()
