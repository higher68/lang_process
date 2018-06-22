#head [-c BYTE] [-n LINE] [FILE...] 
sample_data = open('hightemp.txt', 'r')
samp = []
for line in sample_data:
    samp.append(line.strip('\n'))

n = int(input())
for i in range(n):
    print(samp[i])
