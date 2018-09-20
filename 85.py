# 次元圧縮の手法・・・削ったりクラスターに分けたり。
# その中の一つが主成分分析(PCA)
# 元のデータを変換。その時、最もばらつきが大きくなるものを選ぶ。
from scipy import sparse, io
import sklearn.decomposition

file_in = "84.txt"
file_out = "85.txt"

# 行列読み込み
matrix = io.loadmat(file_in)['matrix_x']

# 次元圧縮
clf = sklearn.decomposition.TruncatedSVD(300)
matrix_to_300 = clf.fit_transform(matrix)
io.savemat(file_out, {'matrix300': matrix_to_300})
