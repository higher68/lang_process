#1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
sampe_data = open('hightemp.txt', 'r')
#cut -f 1 hightemp.txt | sort | uniq cuf -f 1で1列目、sorで整列、uniqは重複なし
#set型使ったら楽そう
samp = []
for line in sampe_data:
    samp.append(line.split())
samp2 = []
for i in range(len(samp)):
    samp2.append(samp[i][0])
for i in range(len(samp)):
    type = set(samp2)
print(type)
