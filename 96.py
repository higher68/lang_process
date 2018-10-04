#  クラスタリング
import pickle
from collections import OrderedDict
from scipy import io
import numpy as np

f_dict_index = "84_dict_index"
f_matrix = "85_matrix_300"
f_countries_plus = "counteriew.txt"

f_dict_new = "96_dict_index"
f_matrix_new = "96_matrix_300"

# 辞書読み込み
with open(f_dict_index, "rt") as data_file:
    dict_index_old = pickle.load(data_file)
# 行列読み込み
matrix_300_old = io.loadmat(f_matrix)["matrix_300"]

# 辞書にある用語のみの行列を作成
dict_index_new = OrderedDict()
matrix_300_new = np.empty([0, 300], dtype=np.float64)
# 0行、300列の行列
count = 0

with open(f_countries_plus, "rt") as data_file:
    for line in data_file:
        try:
            word = line.strip().replace(" ", "_")
            index = dict_index_old[word]
            # np.vstackはndarray同士を結合する。行を追加
            # matrix_300_old[index]]で、単語ベクトルに入力した単語が変換される。
            matrix_300_new = np.vstack([matrix_300_new, matrix_300_old[index]])
            dict_index_new[word] = count
            count += 1
        except:
            pass
# 結果の書き出し
io.savemat(f_matrix_new, {"matrix_300": matrix_300_new})
with open(f_dict_new, "wb") as data_file:
    pickle.dump(dict_index_new, data_file)
