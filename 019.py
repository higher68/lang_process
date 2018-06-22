## 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
from collections import Counter
sample_data = open('hightemp.txt', 'r')
samp1 =[]
for line in sample_data:
    samp1.append(line)
samp2 = []
for line in samp1:
    samp2.append(line.split())
#print(samp2)
samp3 = []
for i in range(len(samp2)):
    samp3.append(samp2[i][0])

mycounter = Counter(samp3)
sorted = sorted(mycounter.items(), key = lambda x:x[1], reverse=True)
for line in sorted:
    print(line)
