import math
from collections import Counter
from collections import OrderedDict
from scypy import sparse, io  # scipy.lil_matrixを使用。0の行列が作られ、0じゃない
# 要素が増えるにつれてメモリの使用量が増えていく

file_corc = "83_CoOccur.txt"
file_word = "83_word.txt"
file_context = "83_context.txt"
file_out = "84.txt"

N = 68031841  # 83本目で求めた定数
# pickle.loadで、保存したファイルを元々のオブジェクトそのものので読み込める。
# ちなみにpickle.dumpを使うと、ファイルに元々のオブジェクトを保った形で保存でき、その作業を直列化とかシリアライズとか呼ぶ
with open(file_corc, "rt") as data_file:
    counter_corc = pickle.load(data_file)
with open(file_word, "rt") as data_file:
    counter_word = pickle.load(data_file)
with open(file_word, "rt") as data_file:
    counter_context = pickle.load(data_file)

# OrderedDictは、要素の順番を保持した辞書
dict_index_word = OrderedDict((key, i) for i, key in
                    enumerate(counter_word.keys()))
dict_index_context = OrderedDict((key, i) for i, key in
                    enumerate(counter_context.keys()))

# lil_matrixを用いた行列の作成
size_word = len(dict_index_word)
size_context = len(dict_index_context)
matrix = sparese.lil_matrix((size_word, size_context))

with open(file_out, "wt") as result_file:
