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


f_in = "combined.tab"  # 2つの結果がマージされたデータ。タブ区切り。
