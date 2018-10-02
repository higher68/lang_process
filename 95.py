
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
    data = list(read_data())

# 順位づけ
data_sorted_by_human_score = sorted(data, key=lambda data: data.human_score)
for order, d in enumerate(data_sorted_by_human_score):
    d.human_order = order

data_sorted_by_my_score = sorted(data, key=lambda data: data.myscore)
for order, d in enumerate(data_sorted_by_my_score):
    d.my_order = order
