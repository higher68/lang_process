import random
file_in = "81.txt"
file_out = "82.txt"


def abs(x):
    '''
    return
    xが0より小さいと0
    0以上だとxを出力
    '''
    if x < 0:
        return 0
    else:
        return x


with open(file_in, "rt") as data_file, open(file_out, "wt") as result_file:
    for line in data_file:
        words = line.strip().split()
        for i in range(len(words)):
            context = []
            width = random.randint(1, 5)
            # 前後width語以内の語の列挙
            for j in range(abs(i-width), i+width+1):
                if j == i:
                    continue
                else:
                    context.append(words[j])
            print(words[i], end="\t", file=result_file)
            print(context, sep="\t", file=result_file)
