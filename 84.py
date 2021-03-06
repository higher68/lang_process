import math
from collections import Counter
from collections import OrderedDict
from scypy import sparse, io  # scipy.lil_matrixを使用。0の行列が作られ、0じゃない
# 要素が増えるにつれてメモリの使用量が増えていく

file_cooc = "83_CoOccur.txt"
file_word = "83_word.txt"
file_context = "83_context.txt"
file_out = "84.txt"
file_dict_word = "84_word.txt"
file_dict_context = "84_context.txt"

N = 68031841  # 83本目で求めた定数
# pickle.loadで、保存したファイルを元々のオブジェクトそのものので読み込める。
# ちなみにpickle.dumpを使うと、ファイルに元々のオブジェクトを保った形で保存でき、その作業を直列化とかシリアライズとか呼ぶ
with open(file_cooc, "rt") as data_file:
    counter_cooc = pickle.load(data_file)
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
matrix = sparse.lil_matrix((size_word, size_context))

# f_tcでループを回す。値が10以上だったら、ppmiを計算。mattrixに格納
# ループを回す際のイテレータは、counter.itemsを使うとキーとvalueのペアの
# リストというかイテレータを作れるのでそれを使う
#  なお、zipとかなしに回せるらしい。ふーん
for token, f_tc in counter_cooc:
    if f_tc > 10:
        token = token.split()
        word = token[0]
        context = token[1]
        f_t = counter_word[word]
        f_c = Counter
        ppmi = max(math.log(N * f_tc/(f_t*f_c)), 0)
        matrix[dict_index_word[word], dict_index_context[context]] = ppmi

# 結果の書き出し
# 行列はio.savematで直列化、io.loadmatで戻すことができる。
# できるファイルはmatlabと互換性質があるとよ。
# 辞書のようにキーを指定して保存
io.savemat(file_out, {'matrix': matrix})
with open(file_dict_word, "wt") as result_file1, \
     open(file_dict_context, "wt") as result_file2:
    pickle.dump(dict_index_word, result_file1)
    pickle.dump(dict_index_context, result_file2)
