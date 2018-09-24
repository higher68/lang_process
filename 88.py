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
