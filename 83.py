# 出現回数・・・collectionでいける
# 共起回数・・・単語tと文脈語cのペアが何回出てくるか
# 文脈語の出現回数・・・collectionでいける
#  ペアの出現回数・・・まあ、これもcollectinoでいけるね。
from collections import Counter


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
    for line in data_file:
        words = line.strip().split("\t")
        list_word.append(words[0])
        list_context.append(words[1:])

        # Counter型はupdateで値を追加する
        count_word.update(list_word)
        count_context.update(list_context)

    co

with open(file_CoOccur, "wt") as data_cooc, \
    open(file_word, "wt") as data_word, \
        open(file_context, "wt") as data_context:
    aaa
