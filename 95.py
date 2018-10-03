
f_in = "94_combined_sim.tab"


class Data:
    def __init__(self, human_score, my_score):
        self.human_score = human_score
        self.my_score = my_score


# データの配列作成
with open(f_in, "rt") as data_file:
    def read_data():
        for line in data_file:
            word1, word2, human_score, my_score = line.split()
            yield Data(float(human_score), float(my_score))
    # Dataインスタンスのリストを作成
    data = list(read_data())

# 順位づけ
# human_scoreを基準にソート
data_sorted_by_human_score = sorted(data, key=lambda data: data.human_score)
# shallow-copy?
# ループの中で、orderはindex番号、dはソートされたDataインスタンスのリストの各要素
for order, d in enumerate(data_sorted_by_human_score):
    d.human_order = order
# human_scoreを基準にソート
data_sorted_by_my_score = sorted(data, key=lambda data: data.myscore)
for order, d in enumerate(data_sorted_by_my_score):
    d.my_order = order

# スピアマン相関係数算出
N = len(data)
total = sum((d.human_order-d.my_order) ** 2 for d in data)  # dataの中身でループ
result = 1-(6*total)/(N ** 3 - N)

print(result)
