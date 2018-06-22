#自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
#split -l 行数 ファイル名 [プリフィックス(出力ファイル)]
n = int(input())
sample_data = open('hightemp.txt', 'r')
samp = []
for line in sample_data:
    samp.append(line.strip('\n'))
st = 0
for i in range(len(samp)):
    print(samp[i])
    if (i+1)  % n == 0 :
        print('-------------------')
