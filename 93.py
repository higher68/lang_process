f_in = "92_family_out.txt"

with open(f_in, "rt") as data_file:

    correct = 0
    parent = 0
    for line in data_file:
        cols = line.split()
        parent += 1
        # 正解判定
        # なんで3と４なんだっけ
        # question-wordsの構成は
        # 1語目-2語目+3語目=4語目という形になってる。だからだね。
        # https://qiita.com/Hironsan/items/8f7d35f0a36e0f99752c
        if cols[3] == cols[4]:
            correct += 1
# 正解率表示
print("{} ({}/{})".format(correct / parent, correct, parent))
