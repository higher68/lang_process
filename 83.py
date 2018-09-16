# 出現回数・・・collectionでいける
# 共起回数・・・単語tと文脈語cのペアが何回出てくるか
# 文脈語の出現回数・・・collectionでいける
#  ペアの出現回数・・・まあ、これもcollectinoでいけるね。
from collections import Counter
# ファイル定義
file_in = "82.txt"
file_CoOccur = "83_CoOccur.txt"
file_word = "83_word.txt"
file_context = "83_context.txt"
n = 0
# 共起、単語、文脈語のCounter作成
count_cooc = Counter()
count_word = Counter()
count_context = Counter()
list_cooc = []
list_word = []
list_context = []
with open(file_in, "rt") as data_file:
    # メモリとプロセス削減用にthresholdを儲けて、それを超えたらcounterに突っ込む
    for i, line in enumerate(data_file):
        # \t分割されたデータを分解。それぞれリストに格納
        words = line.strip().split("\t")
        list_word.append(words[0])
        list_context.append(words[1:])
        for i in range(1, len(words)):
            list_cooc.append([words[0], words[i]])

        # Counter型はupdateで値を追加する
        # 格納したデータをcounterで数えていく。
        # 逐一追加すると、計算量がかかるので、一定以上溜まったらね。
        if i % 10000 == 0:
            count_word.update(list_word)
            count_context.update(list_context)
            count_cooc.update(list_cooc)
            list_cooc = []
            list_word = []
            list_context = []
            print("{} column done".format(i))

# あぶれたものを追加
count_word.update(list_word)
count_context.update(list_context)
count_cooc.update(list_cooc)
# 計算結果の書き出し
with open(file_CoOccur, "wt") as data_cooc:
    list_cooc = list(count_cooc.items())
    list_cooc = sorted(list_cooc, key=lambda x: x[2])
    for i in range(len(list_cooc)):
        print("{} {} {}".format(list_cooc[i][0], list_cooc[i][1],
                                list_cooc[i][2]))
with open(file_word, "wt") as data_word:
    list_word = list(count_word.items())
    list_word = sorted(list_word, key=lambda x: x[1])
    for i in range(len(list_word)):
        print("{} {}".format(list_word[i][0], list_word[i][1]))
with open(file_context, "wt") as data_context:
    list_context = list(count_context.items())
    list_context = sorted(list_context, key=lambda x: x[1])
    for i in range(len(list_context)):
        print("{} {}".format(list_context[i][0], list_context[i][1]))
print("N:{}".formta(len(list_context)))
