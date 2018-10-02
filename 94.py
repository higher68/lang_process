import pickle
from collections import OrderedDict
from scipy import io

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


f_in = "./wordsim353/combined.tab"  # 2つの結果がマージされたデータ。タブ区切り。
f_dict = "84_dict_index"
f_matrix = "85_matrix_300"
f_out = "94_combined_sim.tab"

with open(f_dict, "rt") as data_file:
    dict_index = pickle.load(data_file)

matrix_300 = io.loadmat(f_matrix)["matrix_300"]

with open(f_in, "rt") as data_file, \
     open(f_out, "wt") as out_file:
    header = True
    for line in data_file:
        if header is True:
            header = False
            continue
        cols = line.split()
        try:
            dist = cos_sim(matrix_300[dict_index[cols[0]]],
                           matrix_300[dict_index[cols[1]]])
        except KeyError:
            # 単語がなければ-1で出力
            dist = -1
        print("{}\t{}".format(line.split(), dist, file=out_file))
