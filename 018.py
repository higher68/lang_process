#各行を3コラム目の数値の降順にソート
sample_data = open('hightemp.txt', 'r')
samp = []
for line in sample_data:
    samp.append(line.strip('\n').split())
a = sorted(samp, key = lambda x:x[2], reverse=True)
#lambdaが使われるのは、sampの各行の2列目とかを指定するのが無理だからだろうなあ。うーん
for chr in samp:
    c1 =''
    for c2 in chr:
        c1 += c2 +' '
    c1.strip(' ')
    #c1 += '\n'
    print(c1)
