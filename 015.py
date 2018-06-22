#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
#tail [オプション ･･･] ファイル名 [ファイル名2 ･･･]
sample_data = open('hightemp.txt', 'r')
n = int(input())
samp = []
for line in sample_data:
    samp.append(line.strip('\n'))

##rangeの負方向へのループ。かと思ったら、tailは負方向じゃなかった。
for i in range(-n,0):
    print(samp[i])
