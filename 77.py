f_result = 'result.txt'


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
