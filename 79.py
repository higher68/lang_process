import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

f_result = "result.txt"
f_work = 'work.txt'


def scores(fname):
    '''結果ファイルからスコアを算出
    結果ファイルを読み込んで、正解率、適合率、再現率、F1スコアを返す

    return:
    正解率,適合率,再現率,F1スコア
    '''
    # 結果を読み込んで集計
    TP = 0  # True-Positive  予想が+1, 正解も+1
    FP = 0  # False-Positive 予想が+1, 正解が-1
    TN = 0  # True-Negative 予想が-1, 正解も-1
    FN = 0  # False-Negative 予想が-1, 正解が+1

    with open(fname) as file_in:
        for line in file_in:
            cols = line.split('\t')

            if len(cols) < 3:
                continue  # 結果が格納されてないとスキップ

            if cols[0] == '+1':  # 1列目は正解
                if cols[1] == '+1':  # 2列目は予測
                    TP += 1
                else:
                    FP += 1
            else:
                if cols[1] == '+1':
                    FN += 1
                else:
                    TN += 1
    # 算出
    accuracy = (TP + TN) / (TP + FP + FN + TN)      # 正解率
    precision = TP / (TP + FP)      # 適合率
    recall = TP / (TP + FN)     # 再現率
    f1 = (2 * recall * precision) / (recall + precision)    # F1スコア

    return accuracy, precision, recall, f1


# 以下でthreshholdを変えて、各スコアを計算し直す
# 学習結果は使い回し。
# 学習結果の格納
with open(f_result) as f_in:
    for line in f_in:
        values = line.split()
        cols1 = []
        cols2 = []
        # 正解ラベル
        cols1.append(values[0])
        # 正解確率
        if values[1] == '+1':
            cols2.append(float(values[2]))
        else:
            cols2.append(1.0-float(values[2]))
# thresholdを変えながら描画用のデータをセット
thresholds = []
accuracys = []
precisions = []
recalls = []
f1s = []
# np.arrange(start, stop, step)
for threshold in np.arrange(0.02, 1.0, 0.02):
    thresholds.append(threshold)
    with open(f_work) as f_out:
        for label, val in zip(cols1, cols2):
            # 予測、結果出力
            if val > threshold:
                f_out.write('{}\t{}\t{}\n'.format(label, '+1', val))
            else:
                f_out.write('{}\t{}\t{}\n'.format(label, '-1', 1-val))
    accurcy, precision, recall, f1 = scores(f_work)
    accuracys.append(accurcy)
    precisions.append(precision)
    recalls.append(recall)
    f1s.append(f1)

# グラフ描画
plt.figure()
plt.plot(thresholds, accuracys, precisions, recalls, f1s)
plt.xlim(0, 1.0)
plt.legend("正解率", "予測率", "適合率", "F１スコア")

plt.show()
